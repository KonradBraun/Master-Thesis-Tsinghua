# Triage — `Literature/Potential/` (17 Oct 2026)

Based on title + abstract only (from `Potential/txt/`). **A** = read in detail now · **B** = read the relevant section when writing that chapter · **C** = probably not needed.
None of these are in Zotero yet except Liu 2024 (halloysite, already in Zotero). Short names = file names.

## A — read now (parameters, core physics, step 2) — done 17 Oct, values in `../notes/parameters.md`
Note: the 1951 diffusion paper covers only 0.001–0.005 M; the Zn "deviations" paper uses alkaline zincate for its Sand's-time part.
| File | Why |
|---|---|
| diffusion_zinc_sulfate (1951) | **Measured D of ZnSO₄ vs concentration** → replaces placeholder D |
| X-Ray Diffraction … Ion-Pairing in ZnSO4 | ~40 % inner-sphere ZnSO₄ ion pairs at 2.98 M → limits the "ideal, fully dissociated" assumption |
| Raman Spectroscopy of Aqueous ZnSO4 | ion pairing / hydrolysis — same question, second source |
| Electrolyte formulas of aqueous zinc ion (review) | physical electrolyte properties (conductivity etc.) |
| The role of glass fiber separators on the cycling of zinc metal anodes | compares Whatman GF/A–D (pore size, thickness?) → **GF/D parameters** |
| Measuring Zn Transference with Precision | t₊ measurement in Zn electrolytes — directly relevant to F13 |
| Designing single-ion conductive electrolytes (Zn) | t₊ vs σ trade-off, critique of t₊ test methods |
| Dendrite Growth on metal Anodes (unified framework) | Sand's time + kinetics in one model |
| Dendritic growth in zinc electrodeposition – Deviations … | Zn-specific Sand's time, H₂ co-evolution delays dendrites |
| Validity of the Boltzmann equation to describe Donnan equilibrium | Donnan model validity → physics of step 2 |
| Nanodiamonds in Filtration and Adsorption Systems (review 2026) | ND surface charge / chemistry in water → plausibility check step 2 |
| Positive zeta potential of nanodiamonds | ND zeta potential sign depends on surface (sp²) — matters for "fixed negative charge" |

## B — read the relevant part when writing
| Topic → chapter | Files |
|---|---|
| Sand's time (3.4) | A Modified Sand's Time … (Li/SEI) · MODIFICATION TO THE SAND'S APPROACH (PhD thesis, Akolkar group) |
| t₊ methods (3.4) | Accurate characterization of transference numbers · Bruce–Vincent … from molecular dynamics |
| Donnan / charged membranes (4.6) | Donnan equilibrium and dielectric exclusion (2002) · Comparative Analysis of Donnan Steric Partitioning … |
| Charged / ion-selective separators (3.5, 5.2) | Cationic … nanocellulose separators (Zn, t₊ 0.73) · Bioinspired Separator with Ion-Selective Nanochannels (Li) · Improving Ionic Conductivity and Li-Ion Transference (**SI only — main paper missing**) |
| Modified GF separators, comparison table (3.5) | Multiscale Ion-Sieving Separator · Bacterial cellulose mixed with glass fiber · Electro-ionically conductive functional separators · Mechanically robust and water-trapping separators · Regulating the interface chemistry of separator · Ion-Sieving Separator Functionalized by (already in Zotero) |
| ND synthesis — group's own work (3.6) | Silicon-Mediated Laser Shock Synthesis of … (ACS Nano 2026: ~5 nm ND, XPS sp²/sp³/C–O/C=O, no zeta) · Upgrading carbonaceous materials (Zang review, coal context) |
| ZnSO₄ transport data (parameters) | Transference Numbers … Zinc Sulfate (Purser & Stokes 1951) · Mutual Diffusion Coefficients of Aqueous ZnSO₄ (Albright & Miller 1975) · Ion Pairing and Redissociation … (Price & Weingärtner 1991) · Electrical Conductivity of Concentrated … Divalent Metal Sulfates (Bešter-Rogač 2008) · Ion hydration and association … (Buchner & Hefter 2023) · AN ELECTROCHEMICAL STUDY OF ZINC DEPOSITION (Zouari & Lapicque 1992) · Probing Kinetics Beyond Tafel (Rana et al.) — all read, values in `../notes/parameters.md` |
| ND surface chemistry (3.6) | Surface Chemistry of Nanodiamonds (2004) · Surface properties of hydrogenated nanodiamonds · Understanding the Surfaces of Nanodiamonds · Rapid … adsorption … thermally oxidized nanodiamond |
| Phase-field Zn dendrites (4.7, 5.3 — only if in scope) | A Phase-Field Model of Dendrite Growth of (Zn, 2019) · Phase-field modeling of zinc dendrites growth · Toward Quantitative Phase-field Modeling · Understanding Zn Electrodeposits Morphology · Unraveling zinc dendrite growth · Dynamics of zinc dendritic growth (flow battery) · Computer Simulation of Dendritic (1985, historical) |
| Continuum models of Zn deposition (5.1) | NONISOTHERMAL SIMULATION OF (Zn in ZnSO₄, FEM + KMC) |
| Zn plating behaviour (2.5) | Revealing Zn stripping and plating behavior in ZnSO4, Zn(ClO4)2, ZnCl2 |
| V&V (4.8) | Verification and validation in computational (Babuška & Oden 2004) · Concepts of Model Verification and Validation (LANL report) · VER IF ICAT ION AND VAL IDAT ION IN (**only book front matter**) |
| Cathode (2.4) | Recent Advances … Manganese Dioxide · Rechargeable Zn–MnO2 Batteries |
| Manufacturing chapter (option) | Continuous Roll-To-Roll Coating and Drying of (separators, TUM) · Scalable aqueous-phase fabrication of rGO (R2R vs vacuum filtration) · A facile method to enhance the uniformity and adhesion … · Enhancing Li-Ion Battery Performance with Alumina-Coated Separators · Fabrication Techniques for Graphene Oxide-Based Membranes |

## C — probably not needed
Added 17 Oct (group papers): Two-dimensional quantum-sheet films (MoS₂, off-topic) · Electronic, Structural, and Magnetic Upgrading of Coal-Based Products (laser annealing, only marginal for 3.6)
Earlier:
Bimetallic MOF glass fiber (Li–S) · Current density driven texture evolution in zinc powder anodes · Multifunctional pH-Controlling Electrolyte · The magnetohydrodynamic effect (alkaline) · Flexible electrodes review · Scalable Manufacturing of (MXene films) · Validating Computational Models (social-science models) · Transverse Number Measurement (**scanned OneNote notes, no text**)

## Gaps still open
- ~~Bulk conductivity, Zn kinetics~~ — found (see `../notes/parameters.md`)
- **Continuum/FEM models of separators in metal batteries** (Ch. 5) — only one weak Zn paper so far
- **Separator heterogeneity / pore-scale or 2D models of current focusing** (for the 2D homogenisation step) — new since 19 Oct
- **Thermodynamic factor ZnSO₄** (Pitzer & Mayorga 1974) — for CET
- *(option)* Zn corrosion/HER modelling in mildly acidic electrolytes
- **Motivation** (Ch. 1: grid storage, Li-ion limits) — nothing yet
- Oberkampf & Roy book chapters, main paper of the Li-separator SI
