# Paper Summary — ND@GF Separator Manuscript

**"Crystal facet and surface termination co-engineering of nanodiamond-decorated glass fiber separators for durable aqueous zinc-ion batteries"**

| | |
|---|---|
| Journal | Journal of Power Sources — **under review** (as of 30 Oct 2026) |
| Manuscript no. | POWER-D-26-05609 |
| First author | Zhenghe Zhang (Tsinghua ME) — equal contribution with Jiangtao Yuan (SEU), Zhongqi Wei (CUMT-B) |
| Corresponding | Xining Zang (Tsinghua), Zhijun Zhang (CUMT-B), Wenshu Chen (SEU) |
| Files | `POWER-D-26-05609 (2).pdf`, `Supporting Information.docx` |

---

# 1. Methods (from SI)

## 1.1 COMSOL (SI §1.7)

| Setting | Value |
|---|---|
| Geometry | "simplified **2D axisymmetric** electrodeposition model" — planar Zn anode, electrolyte, separator |
| Physics | **Secondary current distribution** + **transport of diluted species**, coupled |
| Anode BC | **constant cathodic overpotential of 0.5 V** |
| Counter electrode | ground potential |
| Lateral boundaries | insulating |
| Initial c(Zn²⁺) | 2000 mol m⁻³ (2 M) |
| **ND representation** | **"uniformly dispersed hollow circles … on the anode-facing side of the glass fiber substrate"** (main text also places the ND layer "between the separator and the zinc anode" in the real cell) |
| Mesh | structured quadrilateral, local refinement at interfaces |
| Solution | **steady-state** |
| Outputs | electric field intensity, Zn²⁺ concentration near anode |

## 1.2 DFT (SI §1.8)

| Setting | Value |
|---|---|
| Code | **VASP**, PAW |
| Functional | GGA-PBE + Grimme DFT-D3 |
| **Plane-wave cutoff** | **350 eV** |
| k-points | Γ-centred Monkhorst-Pack, "spacing of 0.025 Å" *(units as written are dimensionally odd)* |
| Force convergence | 0.05 eV Å⁻¹ |
| Energy convergence | 10⁻⁶ eV |
| Vacuum | 20 Å |

Supercells:
- **Dia. (111):** 12.589 × 13.083 Å, 8.7 Å thick, **5 carbon layers**
- **SiO₂ (001):** 14.295 × 14.295 Å, 14.2 Å thick
- **SiO₂ (111):** 20.216 × 17.507 Å, 10 Å thick
- **Dia.-O (111): not given**

Formulas:
- `E_ads = E_total − E_substrate − E_adsorbate` (isolated adsorbate)
- `Δρ = ρ_total − ρ_substrate − ρ_adsorbate`
- Desolvation: *"implicit solvation model, where a supercell containing 20 water molecules simulated the electrolyte environment"*, with
  `ΔE_desolvation = −ΔE_solvation`, `ΔE_solvation ≈ E(Zn²⁺@solvent) − E(solvent) − E(Zn²⁺(g))`

**Still not stated:** SiO₂ polymorph; whether silica was hydroxylated; termination of "pristine" Dia. (111); charge state and any charged-cell correction; adsorption sites tested; any convergence testing.

## 1.3 Experimental setup (SI §1.1–1.6)

| | |
|---|---|
| Separator | **Whatman GF/D** |
| Zn foil | **100 µm**, 99.9%, Φ10 mm |
| Electrolyte (half cells) | **2 M ZnSO₄** |
| Cells | CR2032 coin cells; Zn//Zn, Zn//Cu, Zn//Ti (LSV), CP//CP (conductivity) — all electrodes Φ10 mm (CP laser-cut). Separator diameter, spacer, spring not stated |
| Full cells | Zn and MnO₂-on-carbon-paper Φ12 mm, 1–2 mg cm⁻² active mass, **1 M ZnSO₄ + 0.1 M MnSO₄** (different electrolyte from half cells) |
| ND application | ND dispersion in DI water, **vacuum-filtered onto GF** (so NDs likely partly enter the GF from the filtration side — inference); main text: NDs "fill the large voids of GF", pores <10 nm (S2c) |
| Cathode | MnO₂-birnessite, synthesised from MnSO₄ + NaOH + H₂O₂ |
| Full cell window | 1.0–1.85 V |
| Rest before test | 6 h |
| EIS range | 100 kHz – 0.01 Hz |
| t₊ method | Bruce-Vincent (chronoamperometry + EIS), ΔV = 10 mV |
| σ method | σ = L/(A·R), CP//CP symmetric cells |
| Eₐ method | Arrhenius fit of R_ct from variable-temperature EIS, Zn//Zn |
| ND synthesis | coal + Si nanoparticles, ball-milled, pressed, dehydrogenised, then 1064 nm laser (500 W, 5 mm spot, 10 mm s⁻¹) through 7 mm water layer; 4 runs × 28 scans; product split across **five** separators |
| **ND loading** | ⚠️ **never stated** — no wt%, no mg cm⁻², no yield |

**Derived — depth of discharge:** 100 µm Zn ≈ **58.5 mAh cm⁻²** areal capacity. Cycling at 1 mAh cm⁻² is therefore **DOD ≈ 1.7%**; at 10 mAh cm⁻², ≈17%.

---

# 2. Key experimental data

| Property | GF | ND@GF |
|---|---|---|
| Ionic conductivity | 2.83 S m⁻¹ | 2.94 S m⁻¹ (+4%) |
| **Zn²⁺ transference number t₊** | **0.51** | **0.69** |
| **Activation energy Eₐ** | **30.8 kJ mol⁻¹** | **19.3 kJ mol⁻¹** |
| S permeated (H-cell, ICP-OES) | ~17.5 | ~7.5 |
| Zn permeated | ~10 | ~14 |
| Corrosion potential / current | −20 mV / 1.17 mA | −15 mV / 0.56 mA |
| Puncture force | 1.38 N | 1.63 N (+18%) |
| Pore size | up to 14 µm | nanoscale pores <10 nm |
| Zn//Zn @ 2 mA cm⁻² | 47 h | 3738 h |
| Zn//Zn @ 20 mA cm⁻² | 9 h | 280 h |
| Zn//Cu CE | fails at 250 cycles | 99.6%, 1200 cycles |
| Nucleation overpotential | 86.5 mV (text) / 84.5 mV (fig) | 76.8 mV |
| Full cell @ 0.1 A g⁻¹ | lower | 281 mAh g⁻¹ |

## 2b. Data read off figures (all "~")

| What | Where | GF | ND@GF |
|---|---|---|---|
| R_ct (whole cell) at 25/30/40/50 °C | S8, S9 | ~290 / 155 / 130 / 92 Ω | ~282 / 250 / 185 / 152 Ω |
| Bruce–Vincent I₀ / I_s (600 s) | S6a, S6c | ~68.5 / ~40 µA | ~40 / ~34.7 µA |
| Bruce–Vincent R₀ / R_s | S6b, S6d | ~680 / ~1250 Ω | ~355 / ~425 Ω |
| Tafel I_corr (cell current, A = 0.785 cm²) | 2f | 1.17 mA | 0.56 mA |
| Nucleation overpotential @ 20 mA cm⁻² | 3e inset | 158.1 mV | 116.4 mV |
| Voltage at 1–20 mA cm⁻² (rate test) | 3c | readable | readable |
| Max. height after 75 cycles @ 2 mA cm⁻² (CLSM) | 4c, 4f | ~60 µm | ~25 µm |
| Pore size (from SEM) | S3 | 0–14 µm, ~47% <1 µm | ~55% 0–5 nm, ~24% 5–10 nm |
| ND crystallite (one particle only) | S2d | — | ~5–7 nm |
| Paper's COMSOL geometry | 2h/i | domain ~180 µm wide, GF ~55 µm thick, bumps ~29 µm Ø | |
| | S11 | domain ~8 µm wide, bumps ~1 µm Ø, ND circles ~0.15 µm | |

**Derived estimates:** i₀ from R_ct (25 °C, per electrode) ≈ 0.11 mA cm⁻²; from Tafel ≈ 1.5 mA cm⁻² (assumes I_corr ≈ i₀ in a symmetric Zn//Zn cell — inference). Debye length in 2 M ZnSO₄ ≈ 0.1 nm (ideal, full dissociation).

# 3. DFT results (Fig. 5)

| Surface | Bader charge | E_ads Zn²⁺ | E_ads SO₄²⁻ | Desolvation *(read from figure)* |
|---|---|---|---|---|
| Dia.-O (111) | 1.44 \|e\| | −3.91 eV | +1.93 eV | ~0.75 eV |
| Dia. (111) | 0.71 \|e\| | −3.05 eV | −0.10 eV* | ~1.6 eV |
| SiO₂ (111) | 0.35 \|e\| | −1.99 eV | −0.15 eV* | ~3.8 eV |
| SiO₂ (001) | 0.20 \|e\| | −1.94 eV | −0.18 eV* | ~1.9 eV |

\* assignment inferred from word order, not explicit in text.

---

# ⭐ Critical findings

## F1 — The nanodiamonds are modelled as empty holes, so no chemistry enters COMSOL at all

> *"uniformly dispersed **hollow circles** were introduced on the anode-facing side of the glass fiber substrate to mimic the spatial distribution of the coal-derived nanodiamond coating"*

The NDs carry **no material properties whatsoever** — no surface charge, no adsorption, no transference number, no modified kinetics. They are geometric voids.

Consequences:
1. **Not a single DFT result enters the continuum model.** The two halves of the paper are completely disconnected — not weakly linked, *unlinked*.
2. **The model cannot distinguish an O-terminated nanodiamond from a glass bead.** Identical results would follow from any insulating circle of the same size.
3. Therefore **the simulation cannot support the paper's central claim.** The title is "crystal facet and surface termination co-engineering"; the simulation offered as mechanistic proof is blind to both facet and termination. By the paper's own DFT, an H-terminated ND would behave differently — but this COMSOL model would return exactly the same answer.

**Main opening for the thesis** (research question not yet decided): give the ND layer physical properties in the continuum model — in the COMSOL-only plan via a fixed charge calibrated on t₊, not via DFT.

## F2 — The DFT desolvation formula contains no surface

`ΔE_solvation ≈ E(Zn²⁺@solvent) − E(solvent) − E(Zn²⁺(g))`

None of the three terms includes the separator. As written this is the **bulk solvation energy of Zn²⁺ in water** — a property of water, not of diamond or silica — and it cannot produce four different values for four surfaces. Yet Figure 5d reports four values spanning 0.75–3.8 eV.

Also: the method is described as an *"implicit solvation model"* **and** as *"a supercell containing 20 water molecules"* — those are mutually exclusive descriptions.

Magnitude check: the real hydration enthalpy of Zn²⁺ is ≈ −2046 kJ mol⁻¹ = **−21.2 eV**. The reported values are 6–28× smaller.

**Figure 5d is not reproducible as documented.**

## F3 — The DFT never reproduces the paper's own measured activation energy

| | Measured Eₐ | DFT desolvation | Overestimate |
|---|---|---|---|
| ND@GF / Dia.-O (111) | 19.3 kJ mol⁻¹ = **0.200 eV** | ~0.75 eV | ~3.8× |
| GF / SiO₂ (001) | 30.8 kJ mol⁻¹ = **0.319 eV** | ~1.9 eV | ~6× |
| GF / SiO₂ (111) | same | ~3.8 eV | ~12× |

Relative improvement: measured **1.60×**, DFT **2.5–5.1×**.

The comparison is never made in the paper. *(Caveat: Eₐ from R_ct is the overall charge-transfer activation energy, of which desolvation is one component — not strictly the same quantity, but they should agree far better than this.)*

## F4 — The simulated operating point is ~6× the real one
A **0.5 V** cathodic overpotential is applied, while the measured nucleation overpotential is **76.8–86.5 mV**. At 0.5 V the system sits deep in mass-transport limitation, far outside the regime the experiments probe.

## F5 — Wrong physics interface for the claim being made
**Secondary current distribution** assumes uniform electrolyte composition — it solves ohmic drop and electrode kinetics but not concentration gradients. It is coupled to a separate dilute-species interface rather than using **Tertiary Current Distribution (Nernst–Planck)**, which solves potential and concentration self-consistently. For a paper whose entire claim is about *concentration homogenisation*, this is the weaker choice.
**Update (group's `.mph`, received 20 Oct, first look without COMSOL):** the files contain only **Electric Currents** (AC/DC module), stationary — not even secondary current distribution or diluted species. So: pure ohmic conduction, no electrode kinetics, no concentration. Verify in COMSOL.

## F6 — Convergence concerns in the DFT
- **Cutoff 350 eV.** VASP's oxygen PAW has ENMAX = 400 eV; standard practice is ENCUT ≥ ENMAX, often 1.3× for accurate forces. 350 eV is **below the recommended minimum for an oxygen-containing system** — and oxygen termination is the entire point of the paper.
- **5 carbon layers** (8.7 Å) is a thin slab; 6–10 layers with the bottom fixed is more typical.
- **No charged-cell correction mentioned**, although both adsorbates (Zn²⁺, SO₄²⁻) are charged species in a periodic cell.
- No convergence testing reported.
- Dia.-O (111) supercell dimensions omitted.

## F7 — No validation of anything
σ (2.83 / 2.94 S m⁻¹), t₊ (0.51 / 0.69) and Eₐ were all measured. None is compared against the model. Mesh convergence is asserted, not shown.

## F8 — ND loading is still unknown
Even with the full synthesis protocol, no mass, yield or areal loading is given — only "deposited onto five glass fiber separators." **Blocking for a loading-optimisation study.**

## F9 — "2D axisymmetric" may not match the figures
SI says axisymmetric; Figures 2h/2i look like a flat layered rectangle with semicircular protrusions. Under axisymmetry those protrusions would be rings, not hemispheres. Worth checking against the actual `.mph`.

## F10 — Low depth of discharge
DOD ≈ **1.7%** at 1 mAh cm⁻² on 100 µm foil. The 3738 h figure is real but obtained at very low zinc utilisation — a standard critique of this literature, worth stating plainly in the thesis.

## F11 — Figure 5c may contradict the text ⚠️ verify visually
Bar heights in Fig. 5c appear to show large negative SO₄²⁻ adsorption energies on the silica surfaces (~−4.5, −6.5 eV), while the text states −0.10/−0.15/−0.18 eV and +1.93 eV for Dia.-O. Either figure and text disagree or the legend is swapped. **Check the figure directly.**

## F12 — Minor internal inconsistencies
- Nucleation overpotential for GF: 86.5 mV (text) vs 84.5 mV (Fig. 3d)
- Voltage hysteresis: 84.4 mV (text) vs 85.4 mV (Fig. 3b)
- Fig. 3e: caption says 1 mAh cm⁻², plot says 10 mAh cm⁻²

## F13 — t₊ raw data inconsistent with ΔV = 10 mV ⚠️ central for step 2
With R₀ ~680 Ω (GF), 10 mV allow at most ~15 µA; measured I₀ ~68.5 µA → I₀R₀ ≈ 47 mV (ND@GF ≈ 14 mV), both > ΔV. The Bruce–Vincent formula only gives positive t₊ because numerator and denominator are both negative. Recalculated from read-off values: ~0.53 (GF), ~0.77 (ND@GF) vs reported 0.51/0.69. **The calibration target t₊ = 0.69 cannot be verified from the raw data.**

## F14 — No kinetic advantage at room temperature
R_ct at 25 °C is practically equal (~290 vs ~282 Ω, S8/S9); at 30–50 °C ND@GF has the *higher* R_ct. The lower Eₐ comes from a weaker temperature dependence, not faster kinetics. Supports modelling the ND effect via transport (t₊), not via i₀.

## F15 — Cell-to-cell scatter unknown but large
Two GF cells: R_ct at room temperature ~290 Ω (S8) vs ~680 Ω (S6b) — as large as the GF vs ND@GF difference. No repeats or error bars anywhere. i₀ estimates from R_ct and Tafel differ ~13×.

## F16 — The paper's COMSOL figures don't match each other
Fig. 2h/i (20 µm scale bar) and S11 (1 µm scale bar) show the same layout at scales ~25–30× apart. S11b shows a uniform c ≈ 1.82×10³ mol m⁻³ with no gradient towards the depositing anode.

## F17 — ND-layer pore size uncertain
SEM (S3b) claims mostly <10 nm pores; BET (S4b) shows identical distributions for GF and ND@GF. Whether SEM at this magnification resolves <5 nm pores is doubtful (inference). Matters because the Debye length (~0.1 nm) limits any surface-charge effect to nm-sized pores.

## F19 — Plain-GF t₊ (0.51) is far above the bulk electrolyte value (0.20)
Bulk 2 M ZnSO₄: t₊ = 0.197 (Purser & Stokes 1951, EMF method). A neutral glass-fibre separator with µm pores should not raise t₊ noticeably. The group's 0.51 (Bruce–Vincent, Fig. 2b) is therefore either a method artefact (cf. F13; literature reports Bruce–Vincent scatter of 0.2 vs 0.7 for near-identical Zn electrolytes) or measures a different quantity. The GF → ND@GF *difference* may still be meaningful; absolute values should not be used as model inputs.

## F20 — XPS fit does not separate sp² from sp³
ND@GF paper (Fig. 1c) fits C 1s with only C–C (284.8 eV, assigned to sp³ diamond) and C–O (286.1 eV). The group's own ND synthesis paper (Zhang et al., ACS Nano 20 (2026) 20231) fits sp² (~284.3–284.6 eV), sp³ (~285.0 eV), C–O and C=O separately and reports "enhanced" sp³ after laser shock — i.e. sp² remains. Matters for the sign of the ND surface charge (sp² → positive zeta potential, Ginés et al. 2017).

## F21 — Fig. 2h/i compare at constant voltage and show only the field
- Simulated at 0.5 V overpotential, experiments run at constant current (2 mA/cm²). The NDs as insulating holes raise the resistance → at equal voltage less total current in (i), so a weaker/smoother field partly just means less current.
- At 0.5 V kinetic resistance is negligible → near-primary (geometry-dominated) distribution → strongest possible tip effect. At the real ~80 mV the reaction resistance evens out the distribution (Wagner number) — the tip effect in (h) is exaggerated.
- Field in the electrolyte is a proxy; the relevant quantity is the current density on the Zn surface (not shown).
- Rough own estimate: field ~4.5×10³ V/m in the separator × σ 2.83 S/m → ~1 A/cm² (if the model used that σ), ~600× the experiment.

## F18 — Further inconsistencies
- Fig. 4a: GF anode "after 75 cycles at 2 mA cm⁻²", but the GF cell short-circuits after ~47 h ≈ 47 cycles (Fig. 3d).
- Fig. 6a: current axis in "A" (up to 0.6 A) — implausible for 1–2 mg cm⁻² cathode, likely mA.
- Fig. 2c: GF permeate S:Zn molar ≈ 3.6:1 — not ZnSO₄ stoichiometry.
- Fig. 2d: applied potential of the chronoamperometry not stated.
