# Thesis Proposal — Outline (DRAFT, 14 Oct 2026)

**Status:** draft structure without DFT (COMSOL only, decided 14 Oct). Deadline: **mid-December 2026** (student, 30 Oct); template: ThuThesis 选题报告 (18 Oct). Length and governing institution **not confirmed** — ~40 pages is the student's estimate.
**Reuse:** Chapters 2–4 should carry over into the thesis almost unchanged.

**Decided (30 Oct):** chapter cut (a) — fundamentals separate from the simulation state of the art, as below; funnel AZIBs → separators/NDs → modelling → state of the art of simulation → gap. Writing directly in English (discussions partly in German). Critique of the group's paper only through our own simulation results — no statements that their measurements/calculations are wrong.

**Open options** (student decides):
- Full cell / cathode: open — half cell first; depends on scope and available data (30 Oct)
- Phase-field section: only if dendrite growth is simulated — undecided
- **Manufacturing chapter (proposed 17 Oct, not yet discussed with supervisor):** one thesis chapter after the design study — tolerances and process window for the ND coating, sensitivity/UQ of which process parameter matters most. Gives the RWTH Produktionstechnik link without bending the topic.

---

## 1. Introduction and Motivation — ~3 p
- Grid-scale storage: requirements (cost, safety, cycle life — not energy density)
- Limits of Li-ion for stationary storage
- Aqueous zinc-ion batteries as a candidate
- Objective and structure of this work

## 2. Fundamentals: Aqueous Zinc-Ion Batteries — ~8–10 p
- 2.1 Working principle and cell components
- 2.2 Comparison with Li — **AZIBs are the zinc analogue of Li-*metal*, not Li-ion**
- 2.3 Electrolyte: water window, Zn²⁺ solvation and desolvation, why mildly acidic sulfate
- 2.4 Cathode materials — brief, MnO₂ *(depth depends on full-cell scope)*
- 2.5 Zinc metal anode: plating/stripping, dendrites, HER, corrosion/ZHS, dead zinc, **how the failure modes feed each other**
- 2.6 Performance metrics and how to read them — incl. the **depth-of-discharge critique**

→ partly drafted in `../Reference/grundlagen-zink-ionen-batterien.md`

## 3. Separators in Aqueous Zinc-Ion Batteries — ~8–10 p *(core of the fundamentals)*
- 3.1 Function and requirements
- 3.2 Li-ion separators for contrast (PP/PE/PP, why they fail in water)
- 3.3 Glass fibre: why it is the standard and why it is inadequate
- 3.4 Ion transport in porous separators
  - porosity, tortuosity, effective properties, MacMullin number
  - **transference number t₊**, ion selectivity, **Donnan exclusion**
  - **Sand's time** — the quantitative link from t₊ to dendrite onset
- 3.5 Modification strategies — state of the art, **comparison table** of modified GF separators (start: manuscript Fig. 3f and refs [13, 27–33])
- 3.6 Nanodiamonds: structure and facets, H vs O termination, synthesis (incl. coal/laser shock), prior use in zinc batteries (all anode-focused, refs [17–19])

## 4. Fundamentals: Continuum Electrochemical Modelling — ~8 p
- 4.1 Length scales; why atomistic methods (DFT) are out of scope — ~½ page
- 4.2 Nernst–Planck transport, electroneutrality
- 4.3 Butler–Volmer kinetics, exchange current density
- 4.4 **Current distribution classes** — primary / secondary / tertiary, when each is valid
- 4.5 Porous media: homogenisation, effective properties
- 4.6 **Charged porous layers** — fixed charge, Donnan equilibrium *(basis for the ND layer)*
- 4.7 *(only if in scope)* Phase-field modelling of electrodeposition
- 4.8 **Verification and validation** — mesh convergence, calibration vs validation

→ partly drafted in `../Reference/grundlagen-simulation.md`

## 5. State of the Art: Simulation of Zinc Deposition and Separators — ~4–5 p
- 5.1 Continuum/FEM models of Zn deposition, field and concentration distribution
- 5.2 Models of separators and charged/ion-selective layers in metal batteries
- 5.3 Phase-field studies of zinc dendrite growth
- 5.4 Atomistic studies — brief context only
- 5.5 The gap: continuum models without physical separator/coating properties

*Needs the most new reading — start early.*

## 6. Research Gap and Objectives — ~2 p
- Starting point: the ND@GF separator and its reported performance
- Gap: the group's COMSOL model represents NDs as "hollow circles" without properties (SI §1.7)
- **Research question — not decided.** Student's working draft (20 Oct, wording open): *Which mechanisms explain the improved cell performance with the ND@GF separator, and how can they be represented in a simulation model?* (Earlier idea "how much ND is needed" dropped after model 03: fixed charge too weak.)
- Sub-objectives and explicit out-of-scope list — *option:* derive manufacturing tolerances / process window for the ND coating

## 7. Methodology — ~4–5 p *(write last)*
- 7.1 Model chain: 1D GF baseline → ND layer with fixed charge → virtual Bruce–Vincent → 2D mechanism models (pore structure, interface, corrosion) → mechanism ranking (see `../notes/progress.md`, approach agreed with the student 30 Oct)
- 7.2 COMSOL model: geometry, Tertiary Current Distribution (Nernst–Planck), BCs, parameters
- 7.3 Calibration and validation: calibrate on GF σ; ND fixed charge estimated physically, not calibrated on t₊ (virtual Bruce–Vincent shows the method's limits in Zn cells); compare trends with measured voltage, nucleation overpotential, interfacial resistance
- 7.4 Design study and sensitivity analysis — *option:* tolerance analysis under process variation (Uncertainty Quantification Module); scripted/automated calibration and parameter studies (Optimization Module, LiveLink for MATLAB)
- 7.5 **Parameter table** — value, unit, source, status (keep as a living file from day one)

## 8. Work Plan and Timeline — ~1–2 p
Gantt chart, milestones, risks and mitigations.

## References
Expect 80–150 entries.

---

# Questions for the supervisor about the proposal
- [ ] Which institution's rules apply — RWTH, Tsinghua, or both? (length, structure, language)
- [ ] Required template or structure? Citation style?
- [ ] Is ~40 pages the expectation? Graded, defence/presentation? (deadline known: mid-Dec)
- [ ] Example proposals from previous students?
- [ ] Depth on simulation fundamentals vs electrochemistry?
- [ ] One committed scope, or alternatives with a recommendation?
- [x] How explicitly to criticise the group's paper — decided by the student (30 Oct): only through own simulation results
- [x] AI use: allowed, no declaration needed (student, 30 Oct)

# Literature workflow
1. Zotero + MCP server; PDFs via Zotero Connector through the library access, so they are attached automatically
2. Per chapter: 1–2 reviews first → their references (backward) → "cited by" (forward) → targeted keyword searches
3. Tags `must-read` → `read`; a 3-line Zotero note per paper (what, key numbers, relevance)
4. Literature matrices for 3.5 (modified GF separators) and Ch. 5 (simulation studies)
5. Reading order: Ch. 3 + 4 first (feed the COMSOL work), Ch. 5 early in parallel, Ch. 2 partly drafted
