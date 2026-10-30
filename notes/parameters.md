# Parameter Table — living file (becomes proposal §7.5)

Status: ✅ sourced · ⚠️ sourced but not directly applicable · ❌ placeholder / gap. Values read off figures marked "~".

**Rule (student, 18 Oct):** group's own measured values come first; literature only where the group has no value or the group value is clearly unrealistic (decided case by case, together). Literature values stay in the table as cross-check — where they differ (e.g. t₊ 0.51 vs 0.20), run both as a sensitivity case.
PDFs not yet in Zotero — add before citing.

| Parameter | Value | Source | Status / note |
|---|---|---|---|
| c₀ | 2000 mol/m³ (2 M ZnSO₄) | group SI §1.5 | ✅ |
| Operating current | 2 mA/cm² (and 20 mA/cm²) | group paper Fig. 3d/3e | ✅ |
| Electrode area | Φ 10 mm → 0.785 cm² | group SI §1.5 | ✅ |
| Separator thickness L | 675 µm (Whatman GF/D, nominal, uncompressed) | **Cytiva, Laboratory filtration product guide (CY53855, Sep 2025), p. 51** · also Hansen et al. 2023, J. Membr. Sci. 688, Table 1 | ✅ nominal · ❌ compressed thickness in the coin cell unknown — ask group which L they used for σ · hint (own, 30 Oct): R_bulk of the ND@GF Bruce–Vincent cell 1.85 Ω (S6 raw EIS) with σ = 2.94 S/m, A = 0.785 cm² → L ≤ ~430 µm (upper bound, contacts add resistance) — consistent with ~430 µm (Hess); the GF cell (7.3 Ω) is not usable for this |
| GF/D mean pore size | 2.7 µm | same | ✅ (group's SEM: up to ~14 µm, Fig. S3) |
| GF/D porosity | **~92 % uncompressed; ~88 % after compression to ~430 µm** (50 N/cm² in coin-type cells) — measured on GF/D 1823-257: 679 ± 21 µm, 41.21 mg per 20 mm disc | Hess, J. Electrochem. Soc. 165 (2018) A323, suppl. note (arXiv 1801.09676) · cross-check: 1 − 121 g/m² / (675 µm × ρ_glass) = 0.92–0.93 for ρ_glass 2.23–2.6 g/cm³ (Cytiva guide p. 51; ρ_glass sources disagree, barely matters) | ✅ · compressed values are from Li cells (titanium coin cells), not the group's CR2032 — use as estimate, ask group for spacer/spring |
| D(Zn²⁺), infinite dilution | ~7.1 × 10⁻¹⁰ m²/s | derived from λ°(½Zn²⁺) ≈ 53.5 S cm²/eq in Harned & Hudson 1951 (JACS 73, 3781) | ⚠️ dilute limit only, not 2 M |
| D(SO₄²⁻), infinite dilution | ~1.06 × 10⁻⁹ m²/s | derived from λ°(½SO₄²⁻) = 79.8 S cm²/eq, same | ⚠️ dilute limit only |
| **t₊ of bulk 2 M ZnSO₄, 25 °C** | **0.197** at 2.0 mol/kg (0.226 / 0.255 / 0.294 at 1.5 / 1.0 / 0.5 mol/kg; limit 0.398 at m → 0) | Purser & Stokes, J. Am. Chem. Soc. 73 (1951) 5650, Table II (EMF method) · cross-check in dilute range: Dye, Faber & Karl, J. Am. Chem. Soc. 82 (1960) 314 (moving boundary, ≤ 0.09 N: T₊ = 0.3892 − 0.0633 √N, agrees with Purser & Stokes) · used by Price & Weingärtner 1991 together with σ and D |  ✅ only source at 2 M (second high-concentration source not found; Hittorf data only in a 1954 PhD thesis) · **≠ group's 0.51 for plain GF** (Bruce–Vincent) — a neutral µm-pore separator should not change t₊ much → supports F13 / F19 |
| **Salt (mutual) diffusion coefficient, 2 M, 25 °C** | **≈ 3.27 × 10⁻¹⁰ m²/s** (Table III: 0.328 / 0.320 × 10⁻⁵ cm²/s at 2.0 / 2.25 mol/kg; interpolated to 2.044 mol/kg) | Albright & Miller, J. Solution Chem. 4 (1975) 809 (Rayleigh interferometry) | ✅ |
| Density / molality conversion | 2 M ≈ 2.044 mol/kg; ρ ≈ 1.30 g/cm³ (2.0248 mol/L at 2.0698 mol/kg: 1.30509) | Albright & Miller, Table II | ✅ |
| Self-diffusion D at ~2 M (≈ 2.05 mol/kg), 25 °C | D(Zn) ~2.1 × 10⁻¹⁰, D(SO₄) ~2.6 × 10⁻¹⁰ m²/s (interpolated; table: Zn 0.277/0.146 at 1.539/2.521 mol/kg, SO₄ 0.269/0.202 at 1.945/2.521 mol/kg, ×10⁻⁵ cm²/s) | Price & Weingärtner, J. Phys. Chem. 95 (1991) 8933, Table III (radiotracer) | ⚠️ self-diffusion ≠ what Nernst–Planck needs: Nernst–Einstein with these gives ~14 S/m vs measured 5.67 (own) — ion association. Paper also reports viscosity, pH (5.55 at 1 mol/kg) |
| t₊ implied by these D | ~0.40 | own calculation | ⚠️ dilute; group measured 0.51 (GF) — and their value is questionable (paper-summary F13) |
| Bulk conductivity of 2 M ZnSO₄, 25 °C | **≈ 5.67 S/m** — ZnSO₄ conductivity maximum κ_max = 5.670 S/m at µ = 1.945 mol/kg (298.15 K); 2 M ≈ ~2.05 mol/kg (density assumed) lies on the flat maximum → 5.66 S/m (own evaluation of the Casteel–Amis fit, a = 0.79331, b = −0.06772) | Bešter-Rogač, J. Chem. Eng. Data 53 (2008) 1355–1359, Table 3; cross-check: CRC table (20 °C) 4.33 S/m at 15 wt% | ✅ **Consequence:** MacMullin number of GF = 5.67 / 2.83 ≈ 2.0 → ε/τ ≈ 0.50 (own). Ideal Nernst–Einstein with dilute D would give ~53 S/m → strong non-ideality |
| Ion association in ZnSO₄ (DRS, 25 °C, up to 2.4 M) | significant ion pairing (SIP + CIP), no double-solvent-separated pairs; overall K_A consistent with literature | Buchner & Hefter, J. Mol. Liq. 383 (2023) 122146 | ⚠️ supports "effective parameters" rather than ideal dissociation |
| Ion pairing in ZnSO₄ | contact-pair K_A ≈ 0.10 (25 °C); X-ray fit ~40 % inner-sphere pairs at 2.98 M (but 0–70 % fit similarly well) | Rudolph et al. 1999 (Raman); Radnai et al. 1982 (XRD) | ⚠️ shows the ideal fully-dissociated model is an approximation |
| i₀ (Zn²⁺/Zn) | start 5 A/m² (estimates ~1–15 A/m² from group's cells) · literature: **0.20 A/cm² = 2000 A/m²** in 1 M ZnSO₄ (fast-scan CV on W ultramicroelectrode, Allen–Hickling; Tafel gave 0.32 A/cm²) | own estimates (paper-summary §2b); Rana, Faisal & Dick, Small Methods 10 (2026) 2500508, doi 10.1002/smtd.202500508 | ❌ **gap / discrepancy ~100–1000×** between intrinsic kinetics (clean UME) and effective values in real cells (foil, surface films). Model needs the effective value → calibrate on Fig. 3c/3d |
| i₀ on a macroscopic Zn electrode (RDE), 25 °C | ~0.02 / 2.5 / 8.7 A/m² at 0.01 / 0.07 / 0.15 M ZnSO₄ (in 0.2 M Na₂SO₄; own evaluation of i₀ = A·exp(−2000/T)); "black-box" D(Zn) ≈ 0.5 × 10⁻⁹ m²/s | Zouari & Lapicque, Electrochim. Acta 37 (1992) 439, Table 2 | ⚠️ dilute, but same order as the group's cell estimates (1–15 A/m²) → supports "effective i₀ ≪ UME value". Strong concentration dependence — no extrapolation to 2 M |
| α_a, α_c | 1, 1 (symmetric, n = 2) | Zouari & Lapicque fix α = 0.5 per electron (α·n = 1) — fit could not separate α and i₀; Rana et al. use α = 0.5 | ⚠️ supported as the standard assumption, not measured for 2 M |
| Temperature | 298.15 K | assumption ("room temperature", Fig. 3) | ⚠️ |
| ND surface groups | ~67 –COOH per 5 nm detonation ND (≈ 0.85 /nm², own conversion) | Shalumon & Stehlik 2026, ACS AMI 18, 47144 (review) | ⚠️ detonation ND, not coal/laser ND |
| ND loading | 0.1–0.4 mg per separator (Φ10 mm → 0.13–0.51 mg/cm²) | group (former postdoc via Yanmei Zhang, 19 Oct) | ✅ |
| ND layer thickness | 30–50 µm, NDs deposited on the glass fibres (not a separate film) | group, 19 Oct | ✅ |
| ND size | ~5 nm average | Zhang et al., ACS Nano 20 (2026) 20231 (pulsed laser; separator paper uses CW laser) | ⚠️ |
| Diamond density | 3.5 g/cm³ | "Understanding the Surfaces of Nanodiamonds" (Literature/Potential) | ✅ |
| ND volume fraction in layer | ~0.7–4.9 % → layer porosity ~0.87–0.91 (own calc.) | from rows above | estimate |
| Fixed charge X in layer | ~13–94 mol/m³ (own calc.: 5 nm spheres, 0.85 COOH/nm² all dissociated → upper bound) | rows above | estimate. **X needed for local t₊ = 0.69 at 2 M (ideal Donnan): ~3100 mol/m³** — ~30–200× more |
| Separator / electrode area | Φ10 mm for separator, Zn, Cu, Ti, CP (A = 0.785 cm²); CP ~50 µm thick | group, 19 Oct + SI §1.5 | ✅ |
| Cell stack | Zn / separator / Zn — no spacer/spring mentioned | group, 19 Oct | ⚠️ compressed thickness still unknown |
| ND@GF zeta potential (group) | ~−38.8 mV (medium/pH not stated; GF reference not given) | group, 19 Oct | ✅ sign negative confirmed |
| ND zeta potential (literature) | air-oxidised ND: −35 mV (pH 3) to −55 mV (pH 11); **positive** when sp² carbon is on the surface (H-ND ~+45 mV) | Ginés et al. 2017, Nanoscale 9, 12549; review above | ⚠️ sign of the group's ND charge is an assumption — sp² content not characterised |

## Open gaps — keep searching (priority order)
1. ~~Bulk conductivity of 2 M ZnSO₄~~ — found (5.67 S/m)
2. **Effective i₀ and α in real Zn foil cells** — intrinsic UME value is ~100–1000× higher than cell-derived estimates → calibrate
3. ~~Salt diffusion coefficient at 2 M~~ — found (3.27 × 10⁻¹⁰ m²/s)
4. ~~Bulk t₊ at 2 M~~ — found (0.197). **Modelling consequence (own):** σ = 5.67 S/m, D_salt = 3.27 × 10⁻¹⁰ m²/s and t₊ = 0.197 cannot all be matched by ideal Nernst–Planck with two ion D's (fitting D_salt and t₊ gives σ ≈ 31 S/m). Needs a concentrated-solution (Newman-type) binary-electrolyte formulation with σ, D_salt, t₊ as separate inputs — COMSOL's "Battery with Binary Electrolyte" is 1:1 only, but **COMSOL 6.3 adds the "Concentrated Electrolyte Transport" interface** (Onsager–Stefan–Maxwell, arbitrary ions with user-defined charges; in Electrochemistry, Battery Design, Electrodeposition, Fuel Cell modules). Inputs are Maxwell–Stefan diffusivities (Zn–H₂O, SO₄–H₂O, Zn–SO₄) → convert from σ, D_salt, t₊ (+ thermodynamic factor, density). Still open: separator t₊ (group), **thermodynamic factor** of ZnSO₄ (activity data, e.g. Pitzer & Mayorga 1974) — needed for the CET conversion; — Bruce–Vincent values scatter strongly (0.2 vs 0.7 for near-identical Zn electrolytes, Gomez Vazquez et al., Adv. Mater. 2025)
5. ~~GF/D porosity~~ found (Hess 2018); compressed thickness ~430 µm only as estimate from Li coin cells — confirm with the group's spacer/spring
6. ~~ND loading / layer thickness, charge sign~~ — from the group (19 Oct). Raw S5/S6 + `.mph` pending ("a few days"). Still unknown: L used in σ = L/(R·A), compressed thickness
