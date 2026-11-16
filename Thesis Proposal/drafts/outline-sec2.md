# §2 paragraph outline (D3) — working draft

Outline notation: "(Dong, Fig. 3a)" only points to the source. In the prose, claims carry the citation; papers as sentence subjects ("X et al. showed") only in the close-to-topic part (§2.4 end, §2.5, §2.6).
Per paragraph: **claim** · evidence with numbers (location in source) · citation keys from `refs.bib`. `(calc)` = own calculation, `~` = read off a figure. Written one section at a time; each section is reviewed by the student before the next one.
Status: structure agreed 12 Nov (§2.1–§2.6, see `../proposal-plan.md`) · §2.1 reviewed 12 Nov (Li-comparison paragraph removed; tags applied), prose written 13 Nov in `../proposal/data/chap02.tex` (with the §2 roadmap), Claude's self-review fixes applied 13 Nov (the prose now deviates from this outline: new paragraph on the measured interfacial pH, Rana 2025), awaiting the student's review · §2.2 drafted 12 Nov, revised after first feedback, tags applied 13 Nov, prose + Table 2.1 written 14 Nov, then condensed to ~2 p + table for the ~20-page budget (unreviewed; source corrections below; long version kept as thesis material in `thesis-material/sec2-2-long-14nov.tex`) · §2.3 prose written 14 Nov directly from the matrix (no outline; ~1.4 p, unreviewed) · §2.4–§2.6 open.
Section numbers differ from `review-matrix.md` and the Zotero `lr-*` tags: matrix/`lr-2.3` NDs → §2.4 here; matrix/`lr-2.4` simulation → §2.3 here.

## §2 opening (roadmap, 3–4 sentences)
**Claim:** The review narrows from the zinc anode problem (§2.1) to separators as one remedy (§2.2) and how such systems have been simulated (§2.3), then to nanodiamonds as the modifier studied here (§2.4) and the group's ND@GF separator as the direct starting point (§2.5); §2.6 states the research gap and what this work does differently.
No citations.

## §2.1 Aqueous zinc-ion batteries and the zinc anode problem
Target ~1.5 pages, 4 paragraphs + roadmap. Function in the argument: set up (a) why the anode limits the cell, (b) which failure processes a separator can address, (c) why reported cycle lives are hard to compare.

**¶0 Roadmap (2 sentences).** Working principle and appeal of the Zn anode → failure processes and how they couple → what follows for test conditions.

**¶1 Why a zinc metal anode.**
- Claim: In mildly acidic aqueous electrolytes zinc can be used directly as a metal anode, which is the main appeal of AZIBs for stationary storage.
- Evidence: Zn 819 mAh g⁻¹ and 5854 mAh cm⁻³, E° = −0.762 V vs SHE (Dong, Intro) · Zn ~US$2 vs Li ~US$19 kg⁻¹ (Cui, p. 1) · realistic cell level 60–80 Wh kg⁻¹ at N/P 2–5 (Dong, abs/Fig. 5e) → stationary rather than mobile use (links back to §1).
- Electrolyte used in this work: 2 M ZnSO₄, mildly acidic — pH 3.3 reported for 2 M (Cui, Tab. 1); 5.55 at 1 mol kg⁻¹ (Price & Weingärtner). ⚠ The two pH values differ more than the concentration difference explains → state as a range, don't pick one.
- Keys: `dong_towards_2022` · `cui_revealing_2025` · `price_ion_1991` · group cite for "reviewed in": `blanc_scientific_2020`, `tang_issues_2019`, `yu_ten_2023`.

**¶2 The failure processes are coupled through the interfacial pH.** (core paragraph of §2.1)
- Opening sentence (from the former Li-comparison paragraph, removed 12 Nov): the anode limits cycle life through non-uniform deposition and dendrites, hydrogen evolution (HER), corrosion and solid by-products; a practical cell needs > 99.9 % CE (Dong, §1.1).
- Claim: HER, by-product formation and dendrite growth are not independent but form a self-reinforcing chain.
- Chain and evidence:
  1. HER is thermodynamically favoured over Zn deposition: E(H⁺/H₂) ≈ −0.20 V vs SHE at pH 3.3 and ≈ −0.33 V at pH 5.55, both well above −0.762 V (calc, Nernst) — Zn deposition proceeds only because HER is kinetically slow on Zn.
  2. Water released or held at the interface during Zn²⁺ desolvation feeds HER (Xu, p. 341; Yu 2024 JACS — abstract not in Zotero, verify before citing).
  3. HER consumes H⁺ → local OH⁻ rises → insulating zinc hydroxide sulfate (ZHS, Zn₄SO₄(OH)₆·xH₂O) precipitates (Dong, Fig. 3a; Cui, XRD Fig. 4).
  4. The insulating deposits make the current non-uniform; Zn grows preferentially on protrusions and over the by-products (Cui, Fig. 5); adsorbed OH⁻/O²⁻ also raise Zn surface-diffusion barriers and nucleate dendrites (Zhang 2024, DFT, abstract).
  5. Dendrites and electrically isolated ("dead") Zn lower CE and can short the cell through the separator (Dong; Xu).
- Closing sentence: the spatial pH field at the anode has not been measured (Dong) → it is a natural target for a continuum model (link to the corrosion/HER option, §4).
- Keys: `dong_towards_2022` · `cui_revealing_2025` · `xu_electrolyte_2023` · `zhang_unveiling_2024` · (`yu_unlocking_2024` only if verified).

**¶3 Remedies and what a separator can address.**
- Claim: Remedies act at the electrolyte, at the interface or on the substrate (e.g. Zn(002)-textured deposition on epitaxial graphene, Zheng 2019) or at the separator. A separator acts on transport — it can make the Zn²⁺ flux and current more uniform and block growth through its pores — but it cannot remove the thermodynamic driving force for HER or corrosion at rest.
- Evidence: Dong names the thick, large-pore GF separator as a cause of uneven deposition (§1.4) · Li 2022 Joule: water activity as the core problem, cathode-side processes (text).
- Consequence (own inference, mark as such): separator papers that report less HER or corrosion need an indirect mechanism (solvation, local pH buffering) → this is examined in §2.2/§2.4.
- Transition to §2.2.
- Keys: `zheng_reversible_2019` · `dong_towards_2022` · `li_toward_2022`.

**¶4 Test conditions and how cycle-life data are compared.** (3–4 sentences, field-wide and neutral — revised 12 Nov)
- Claim: Cycle life and CE of Zn cells depend strongly on the test conditions (Zn utilisation, current density, areal capacity); values are therefore compared only between cells tested under the same conditions.
- Evidence: with 100 µm Zn (≈ 58.5 mAh cm⁻²) most studies use < 1 % of the Zn (Li 2022 Joule, text) · same system: Zn‖Cu ~1000 h at 0.68 % vs ~190 h at 2.9 % Zn utilisation (Dong, Fig. 2b) · with thin Zn the real Zn efficiency per cycle (88.11 % in the example, 20 µm Zn, 3 mAh cm⁻²) is far below the reported CE (Wu 2024, Fig. 3A).
- Consequence for this work (positive): the reference the model has to explain is the comparison of GF and ND@GF under identical conditions → the simulation works at the experimental operating point, 2 mA cm⁻² and 1 mAh cm⁻² (verified 13 Nov: manuscript text to Fig. 3d, "2 mA cm⁻² with a fixed areal capacity of 1 mAh cm⁻²"). Transfer to practical conditions (high Zn utilisation, full cells) is outside the proposal.
- Do **not** mention the group's DOD (1.7 %) or call its result typical — the identical-condition comparison strengthens the paper's result (student, 12 Nov). In the §2.2 table DOD is a neutral column for every paper.
- Keys: `li_toward_2022` · `dong_towards_2022` · `wu_zinc-anode_2024`.
- Moved out: E/C (Xu) and in situ vs coin cells (`yu_ten_2023` → only in the review group cite of ¶1); soft shorts (`li_soft_2022`) and symmetric vs full cell (`guo_non-destructive_2025`) stay in §2.2.

### Proposed `use-*` tags for §2.1 items (applied in Zotero after review)
| Key | Tag | Reason |
|---|---|---|
| `dong_towards_2022` | use-core | carries ¶1–¶4 with numbers |
| `cui_revealing_2025` | use-core | 2 M ZnSO₄ by-products (XRD), pH, cost |
| `xu_electrolyte_2023` | use-core | desolvation water → HER, E/C |
| `li_toward_2022` | use-core | Zn utilisation < 1 %, water activity |
| `wu_zinc-anode_2024` | use-core | capacity inflection, 88 % real efficiency |
| `yu_ten_2023` | use-context | review group cite (¶1) |
| `zhang_unveiling_2024` | use-context | DFT, abstract only, no numbers used |
| `zheng_reversible_2019` | use-context | one example of a substrate strategy |
| `blanc_scientific_2020` | use-context | group cite for reviews |
| `tang_issues_2019` | use-context | group cite for reviews |
| `yu_unlocking_2024` | use-drop | no abstract in Zotero; claim covered by Xu (→ context if verified) |
| `kim_insights_2024` | use-drop | abstract does not support a Zn–Li comparison; paragraph removed anyway |
| `hao_deeply_2020` | use-drop | alkaline vs mild; thesis uses mild electrolyte only |

### Open points for §2.1
- Cui 2025 also gives σ = 4.83 S m⁻¹ and t₊ = 0.35 for 2 M ZnSO₄ (Tab. 1); `parameters.md` uses 5.67 S m⁻¹ (Bešter-Rogač) and 0.197 (Purser & Stokes). Not used in §2.1; the scatter belongs in §2.2/§4.
- pH of 2 M ZnSO₄: kept as a stated range for now (student, 12 Nov); a clearer value/source can be added later.

## §2.2 Separators for zinc metal anodes
Target ~3 pages + comparison table (~¾ page), 6 paragraphs + roadmap. Function in the argument: (a) GF is the common baseline but a poorly defined one, (b) the modifications are many, but their mechanisms are explained with the same four claims and rarely quantified, (c) the reported σ, t₊ and cycle-life numbers allow comparisons within a paper, not across papers → motivates a mechanistic model (§2.3).
Placement: the group's ND@GF manuscript appears here only as a neutral table row (discussed in §2.5); Zhang 2024 ACS AMI (ND@GF precedent) is a table row here and discussed in §2.4. Numbers below come from `../../Literature/review-matrix.md` §2.2 unless marked.
**Prose rule (student, 12 Nov):** explanation over numbers — about 1–2 anchor numbers per paragraph; the table carries the detail. The evidence lists below are the source pool; ★ marks the numbers kept in the prose.
**Thread through §2.2 (raised by the student 12 Nov; framing proposed, not yet agreed):** t₊ is the most reported metric and named as a mechanism almost everywhere, but no paper isolates its effect → raised here from the literature only; our own model results on t₊ and Bruce–Vincent come in §4/§5.

**¶0 Roadmap (2 sentences).** What a separator must do and through which transport quantities it acts → the GF standard and its deficits → modification families and the mechanisms claimed for them → what the reported numbers allow one to conclude (table).

**¶1 Requirements and the transport quantities a separator changes.**
- Claim: A Zn separator must be electronically insulating, wetted by and stable in the mildly acidic electrolyte and strong enough to resist Zn penetration, while adding little ionic resistance. It acts on the anode through three quantities: effective conductivity, Zn²⁺ transference number t₊ and pore structure.
- Evidence: separator classes for AZIBs (polyolefin, solid electrolytes, hydrogel, cellulose, GF) and GF's strengths (wettability, porosity, chemical stability), which made it the benchmark (Gu, §2) · σ_eff = σ·ε/τ (source: Zahn 2016 SI or Lagadec 2018, verify which one states it).
- Why t₊ is pursued: the anion share of the current (t_a = 1 − t₊) depletes Zn²⁺ at the anode; classical Sand's time τ = πD(nFc₀ / 2j·t_a)², dendrite onset when the surface concentration reaches zero; a lower t_a prolongs τ (Yang 2025, classical-Sand section and "Diffusion" section).
- Magnitude at the operating point used here (calc): 2 M ZnSO₄, D_salt 3.27 × 10⁻¹⁰ m² s⁻¹ (Albright & Miller), bulk t₊ 0.197 (Purser & Stokes), 2 mA cm⁻² → ★ τ ≈ 40 h against a plating step of 0.5 h at 1 mAh cm⁻²; a higher t₊ makes τ longer still. The kinetic correction (1 − e^(−j/j₀))² (Yang 2025) is ≥ 0.54 for j₀ ≤ 1.5 mA cm⁻² and does not change the order of magnitude (calc). Yang 2025 also notes that dendrites often appear well before Sand's time at low current. In the prose: one sentence, formula optional. Possible support (found 14 Nov, `rana_electroanalytical_2025` intro p. 2): at 0.2–1 mA cm⁻² and 0.5–1 mAh cm⁻² conditions are typically "underlimiting" in the sense of Sand's model, yet significant HER occurs, and HER-driven precipitation can induce dendrites "as a secondary consequence". Our 2 mA cm⁻² lies just above their low-current range, so cite for the mechanism, not for our operating point.
- Consequence (own inference, mark as such): at the moderate current densities of most tests the electrolyte at the anode is not depleted, so the classical argument for a high t₊ does not apply directly; any t₊ effect would have to act locally (pore-scale current focusing) → taken up again in ¶4/¶5 and tested by the model (§4).
- Keys: `gu_role_2025` · `yang_dendrite_2025` · `albright_mutual_1975` · `purser_transference_1951` · (`zahn_improving_2016` or `lagadec_topological_2018`, after checking).

**¶2 The glass-fibre standard and its deficits.**
- Claim: Borosilicate glass-microfibre filters (mostly Whatman grades) are the de facto separator in laboratory Zn cells. They were designed for filtration and are coarse-pored, thick and mechanically weak, so cells with GF typically fail by Zn growing through the pores.
- Evidence: designed for filtration; four deficits: non-uniform pores → uneven Zn²⁺ flux and by-products blocking pores, low strength and weak fibre bonding, thickness > 250 µm, high water retention (Gu, §2 A–D); the same list in Chen 2026 (text) · GF/A and GF/C 260 µm, GF/B and GF/D 675 µm; pores 1.6 / 1.2 / 1.0 / 2.7 µm for A / C / B / D (Hansen, Tab. 1) · 79 of 80 cells failed by Zn growing through the pores (Hansen, p. 4) · thicker grades and stacking extend life, e.g. GF/B accumulated capacity 45 → 172 mAh cm⁻² when doubled (Hansen, Fig. 2, 4e–h; in 3 m Zn(OTf)₂, not ZnSO₄ → state it) · 2×GF/A 300 h vs GF/A 100 h at 3 mA cm⁻²/3 mAh cm⁻²; the denser GF/F outlasts GF/A (Gu, Fig. 12b; electrolyte to check) · bare GF/C tensile strength 0.3 MPa (Kim, Fig. 3a).
- Consequence: pore size, thickness and stack compression are first-order parameters, and a "GF" result is defined only together with its grade (→ ¶5). No study found varies compression (inference from the papers read).
- Keys: `gu_role_2025` · `chen_tailored_2026` · `hansen_role_2023` · `kim_mechanically_2025`.

**¶3 Modification strategies.**
- Claim: Modified separators coat, fill or replace the GF, and the added materials fall into four families that change different physical properties: fixed charge, pore structure, local electronic conduction or mechanics.
- Families (examples cited as a group):
  (i) charged or ion-selective layers: sulfonated polymer (Sun 2023), carboxylate (Gou 2025), cationic nanocellulose (Zhang 2023), negatively charged oxide nanosheets (Tan 2025), Nafion as the cation-selective limit case (Wu 2021);
  (ii) inorganic fillers and coatings: MOFs (Song 2022; Shao 2025), clay minerals (kaolin, Zhao 2024; halloysite, Liu 2024), dielectric or ferroelectric oxides (BaTiO₃, Liang 2022; HfO₂, Yuan 2025), CeF₃ gradient (Zhao 2025), ZrO₂ felt replacing GF (Cha);
  (iii) carbon: insulating or functional (g-C₃N₄, Luo 2024; NDs → §2.4) vs electronically conductive (vertical graphene, Li 2020; MXene, Su 2022; graphene Janus, Zhang 2022; nanocarbon, Lee 2024);
  (iv) structural: bacterial-cellulose blend (Huang 2025), PVDF + plasma (Kim 2025).
- Routes: growth on every fibre (Song; Luo, ≤ 0.01 mg cm⁻²) · one-side coating (Liu drop-cast; Su spray; Yuan spin) · filling the fibre interspace (Zhao 2024; Liang) · vacuum filtration (Tan; Kim) · free-standing replacement (Huang 56 µm instead of 246 µm; Cha).
- Conductive layers move Zn deposition onto the separator (Lee 2024: Zn plates onto the conductive layers, not onto GF; text, Fig. S4–S6). In the papers read the functional side always faces Zn; none compares orientations (inference).
- Consequence: the family decides what a continuum model must represent — a fixed charge, a pore geometry, an electronically conducting phase or nothing transport-related (→ §2.3).
- Citations in the prose (student, 13 Nov: cite the strongest papers, not 20 for a few sentences): 1–2 full-text examples per family; the comparison table carries the rest. Proposed: (i) `sun_janus_2023`, `tan_multiscale_2025` · (ii) `song_metalorganic_2022`, `liang_novel_2022` · (iii) `luo_regulating_2024` (functional), `lee_hydrophilic_2024` (conductive; carries the deposition-shift claim) · (iv) `huang_bacterial_2025`. Routes: cite only where a sentence needs a specific example. The family lists above are the pool, not the citation list.

**¶4 The mechanisms claimed, and how they are supported.**
- Claim: Across all families the improvement is explained with the same four mechanisms: a homogenised electric field and Zn²⁺ flux, ion sieving (SO₄²⁻ repulsion, higher t₊), faster desolvation and (002)-textured Zn deposition. They are usually supported by DFT energies and qualitative field maps, not by measurements of the quantity the mechanism depends on.
- Evidence: mechanism categories (Gu; Li 2024 Sci. Bull., abstract) · ★ a surface charge (ζ) is measured in only 3 of the full-text papers: Tan −33.8 mV, Zhang 2023 +47 mV, Cha −34.5 mV · Cha's ζ drops from −34.5 mV in water to −5.2 mV in 50 mM ZnSO₄ (Fig. 1c), i.e. the charge is largely screened at 1/40 of the working concentration (in the prose: in words, no values).
- t₊ as the common currency: 14 of the 16 table papers report a higher t₊ for the modified separator and list it among the mechanisms, but in every case t₊ changes together with pore structure, wetting or mechanics, and no paper separates its effect from these (inference from the full texts) · counter-example: a ~9× life gain with only a small t₊ change and σ·t₊ unchanged (Huang, ¶5) · with ¶1 (no depletion at moderate current) → t₊ is used as evidence more than it has been shown to be the cause (inference; this is the thread the thesis picks up).
- Donnan, briefly: excluding SO₄²⁻ by a fixed charge needs a charge density of the order of the salt concentration in the pore water (ideal Donnan, calc; framework: Galama 2013), i.e. mol L⁻¹ at 2 M; the Debye length is ~0.1 nm (calc, ideal) against µm GF pores (Hansen) → charge selectivity is plausible only in nm pores, if at all. Details in §2.3.
- Less HER / corrosion (promise from §2.1 ¶4, phrased cautiously — note the evidence, no verdict): where table papers report it, state on which measurements the claim rests (e.g. linear sweep voltammetry for the HER onset, Tafel plots for corrosion currents) and that the mechanism is inferred, not measured. One or two sentences. Still to do when writing: list which table papers report LSV/Tafel (not yet extracted systematically; Zhao 2024 has an HER-onset figure, Fig. 3c — read the direction before citing).
- Consequence: the mechanisms predict different signatures (ion sieving should lower σ, ¶5), so the reported σ–t₊ pairs can partly test them.
- Keys: `gu_role_2025` · `li_separator_2024` · `tan_multiscale_2025` · `zhang_cationic_2023` · `cha_stable_2024` · `galama_validity_2013` · `hansen_role_2023`.

**Table 2.x (placed with ¶5).** 16 full-text papers with a GF control (or GF replacement) and at least a σ or t₊ pair, ordered by family; the group's manuscript as the last row, below a rule.
- Columns: ref · modification and route · σ GF → mod (mS cm⁻¹) · t₊ GF → mod (method) · Zn//Zn life mod (GF) in h @ j/Q · DOD (calc where the Zn thickness is stated) · simulation. The CE column is dropped (cell types differ).
- Rows: (i) Sun 2023, Tan 2025 · (ii) Song 2022, Shao 2025, Zhao 2024, Liu 2024, Liang 2022, Yuan 2025, Zhao 2025, Cha · (iii) Luo 2024, Zhang 2024 ACS AMI, Su 2022, Zhang 2022 · (iv) Huang 2025, Kim 2025 · group ND@GF.
- Left out: Zhang 2023 (control is anionic nanocellulose, not GF), Li 2020, Gou 2025 and Lee 2024 (no σ or t₊ pair; cited in ¶3/§2.3).

**¶5 What the table shows: the GF baseline is not reproducible.**
- Claim 1: The plain-GF control differs so much between papers that improvement factors refer to different baselines; only differences within one paper are meaningful.
- Evidence: ★ t₊(GF) 0.13–0.55 across 15 papers (Su 2022 0.24 added 14 Nov) (BV or DC polarisation; Cha 0.43 by liquid-junction potential) · σ(GF) 3.0–25.0 mS cm⁻¹ across 11 papers (incl. Zhao 2024's 10.1, Fig. 2f,g — found by T7), ~8× (calc), plus Liu's 66.6 · GF control life ~60–80 h at 1 mA cm⁻²/1 mAh cm⁻² (Luo; Liu) but 110–300 h at 5 mA cm⁻²/1 mAh cm⁻² (Zhang 2024 ACS AMI; Yuan; Cha) — the control lives longer at 5× the current in some papers · the GF grade is named in only 3 of the 16 table papers (Sun GF/A, Kim GF/C, Yuan GF/C in the SI).
- Reference value and limitation (one sentence each, no method critique — decided 12 Nov): bulk 2 M ZnSO₄ t₊ ≈ 0.2 (Purser & Stokes, EMF), and a neutral µm-pore separator should not raise it much (inference) · t₊ values depend on the measurement method and cell, which limits comparison across papers (Gomez Vazquez 2025: 0.2 vs 0.7 for near-identical Zn electrolytes). The detailed Bruce–Vincent discussion, with the virtual Bruce–Vincent result (model 04), goes to §4 (preliminary results) and §5 (key difficulties).
- Claim 2 (one sentence, no numbers in the prose): two studies report separator conductivities above that of the bulk electrolyte, which a porous separator should not reach → implausible, pointing to measurement or reporting errors (one may be a unit misprint). Wording: "implausible", never "impossible" or "wrong" (student, 13 Nov: never overstate). Pool: Liu GF 66.61 (unit printed "mS cm⁻²", Fig. 3c) and Kim's final separator 67.43 mS cm⁻¹ (Fig. 3e; "67.43 S cm⁻¹" in the conclusion) vs bulk 2 M ZnSO₄ 48.3 mS cm⁻¹ (Cui Tab. 1) / 56.7 mS cm⁻¹ (Bešter-Rogač); both use 2 M ZnSO₄ (methods checked); σ_eff = σ·ε/τ < σ (calc, inference).
- Claim 3: There is no consistent σ–t₊ trade-off. σ falls while t₊ rises in 4 papers (Huang, Liu, Sun; Kim's PVDF-only intermediate) but rises with it in 7 (Luo, Cha, Shao, Zhang 2022, Yuan, Zhao 2024; Kim's final separator). Ion sieving by fixed charge would lower σ (inference) → the reported pairs cannot be explained by charge selectivity alone; wetting, electrolyte uptake and measurement effects likely contribute (inference — phrase as such). Huang's ~9× life gain with σ·t₊ unchanged (21 × 0.19 ≈ 17 × 0.23, calc) points to a structural effect.
- Keys: table keys · `purser_transference_1951` · `gomez_vazquez_measuring_2025` · `cui_revealing_2025` · `bester-rogac_electrical_2008`.

**¶6 Test conditions and what stable cycling proves.**
- Claim: The headline results are obtained under mild conditions, and stable symmetric-cell cycling alone does not prove a stable anode.
- Evidence: most headline Zn//Zn runs at 1–5 mA cm⁻² and 1 mAh cm⁻²; where the Zn thickness is stated, ★ the headline DOD is 0.85–3.4 % (Yuan, Liu, Sun, Huang, Kim; calc); Zn thickness or DOD not reported in 9 of 16 table papers (count, re-check when building the table) · high-DOD tests in only 3 papers: Yang 2022 42.7 % (j/Q not in the main text), Shao 42.70 % at 5/5 → 920 h vs ~26 h for GF (calc), Zhang 2022 56 % (220 h at 28.3 mA cm⁻²/28.3 mAh cm⁻² with ≈ 85 µm Zn), which also proposes DOD ≥ 31 % as a benchmark · soft shorts: local Zn contacts let cells look stable — falling overpotential and R_ct, no voltage drop (Li 2022 soft shorts, Fig. 2); the proposed checks (R_ct after pre-cycling, T-dependent Eₐ, Zn//Cu cells) are not reported by any of the separator papers read (inference) · symmetric-cell gains do not transfer directly to full cells (Guo 2025, abstract).
- Do not single out the group's DOD (student, 12 Nov); its row in the table is neutral.
- Closing/transition: the separator literature therefore offers comparative evidence within single papers and mechanism claims backed by DFT and field maps → how such field maps are computed and what continuum models of Zn deposition and separators can resolve (§2.3).
- Keys: `yuan_synergistic_2025` · `liu_ion-sieving_2024` · `sun_janus_2023` · `huang_bacterial_2025` · `kim_mechanically_2025` · `yang_situ_2021` · `shao_selfrecognition_2025` · `zhang_ionsieving_2022` · `li_soft_2022` · `guo_non-destructive_2025`.

### `use-*` tags for §2.2 items (applied in Zotero 13 Nov; checked: each of the 46 `lr-2.2` items has exactly one)
All 46 items tagged `lr-2.2`, plus items from other sections first cited here.
| Key | Tag | Reason |
|---|---|---|
| `hansen_role_2023` | use-core | GF grades, pore sizes, 79/80 penetration failures |
| `gu_role_2025` | use-core | GF deficit list, grade tests, mechanism categories |
| `li_soft_2022` | use-core | soft shorts and the proposed checks |
| `kim_mechanically_2025` | use-core | GF/C strength; σ above bulk; table row |
| `liu_ion-sieving_2024` | use-core | σ above bulk; table row |
| `cha_stable_2024` | use-core | ζ screened in ZnSO₄; non-BV t₊; table row |
| `tan_multiscale_2025` | use-core | measured ζ; table row |
| `zhang_cationic_2023` | use-core | measured ζ (one of 3); FEM with surface charge (§2.3) |
| `huang_bacterial_2025` | use-core | structural gain with σ·t₊ unchanged; table row |
| `yuan_synergistic_2025` | use-core | GF grade, DOD 0.85 %; table row |
| `shao_selfrecognition_2025` | use-core | high-DOD test; table row |
| `zhang_ionsieving_2022` | use-core | DOD 56 %, ≥ 31 % benchmark; table row |
| `yang_situ_2021` | use-core | high-DOD test (42.7 %) |
| `lee_hydrophilic_2024` | use-core | Zn plates onto conductive layers |
| `zhang_modulating_2024` | use-core | table row; ND@GF precedent (§2.4) |
| `song_metalorganic_2022` · `luo_regulating_2024` · `zhao_separator_2024` · `liang_novel_2022` · `zhao_gradient_2025` · `sun_janus_2023` · `su_printingscalable_2022` | use-core | table rows with numbers |
| `li_directly_2020` · `gou_seaweed-inspired_2025` | use-context | family examples; FEM examples (may become core in §2.3) |
| `chen_tailored_2026` | use-context | second source for the GF deficit list |
| `li_separator_2024` | use-context | review, mechanism categories (abstract only) |
| `nian_advancements_2025` · `lee_challenges_2025` | use-context | review group cite (Lee = INT) |
| `wu_cation_2021` | use-context | Nafion as cation-selective limit case |
| `guo_non-destructive_2025` | use-context | symmetric vs full cell, qualitative |
| `wang_deeply_2025` | use-drop | fourth review, redundant |
| `si_ion-sieving_2025` · `chen_robust_2023` · `wang_establishing_2023` | use-drop | family (i) covered by full-text papers |
| `zhang_stabilizing_2024` · `luo_designing_2024` · `wang_zeolite-filled_2026` · `ma_cuiipolydopamine-modified_2023` · `liu_uniform_2022` | use-drop | family (ii) covered by full-text papers; abstract only or no access |
| `cao_universal_2020` · `lin_performance_2023` · `wang_simultaneously_2021` | use-drop | family (iii) covered by full-text papers |
| `li_functional_2023` | use-drop | not GF, abstract only |
| `akram_electro-ionically_2025` | use-drop | not GF; σ–t₊ compilation only in the SI (→ context if obtained) |
| `chen_bioinspired_2023` | use-drop | Li-metal analogue |
| `zhang_zn-ion_2024` | use-drop | layer on Zn, not a separator |
| *other sections:* `yang_dendrite_2025` · `albright_mutual_1975` · `purser_transference_1951` · `bester-rogac_electrical_2008` | use-core | Sand's time; bulk D, t₊, σ of 2 M ZnSO₄ |
| *other sections:* `gomez_vazquez_measuring_2025` | use-core | t₊ method limitation (§2.2), BV discussion (§4/§5) |
| *other sections:* `galama_validity_2013` · `yang_designing_2024` · `lin_accurate_2024` | decide with §2.3 / §4 | not cited in §2.2 (Galama only as Donnan framework) |

### Open points for §2.2
- Source corrections found while writing the prose (14 Nov, full texts re-checked): ζ is reported in ≥ 5 papers, not 3 (Shao, Zhang 2022 added) · Guo 2025 abstract does not support "symmetric-cell gains don't transfer to full cells" → not cited · Cha 2024 not re-checkable (no full text) → its ζ-screening point and table row left out until the PDF is downloaded · Zahn 2016 (Li-ion: surface chemistry raises σ and t₊ at fixed microstructure; t₊ dominates rate capability) is a counterpoint to "ion sieving should lower σ" → cited · Su 2022 tested at 0.01 m ZnSO₄ to make Sand's time short → cited as support · Yuan 2025 showed HER suppression in 2 M Na₂SO₄ (Fig. 3b), a substitution test criticised by Rana AEM → cited · Yang 2025 kinetic correction depends on j₀ (with j₀ ≈ 7–8 mA cm⁻², as reported by Liang/Kim, τ drops to ~2–3 h, calc) → "does not change the order of magnitude" dropped · Zhang 2022 uses 3 m ZnSO₄.
- Group row in the table depends on the supervisor's OK to cite the manuscript (`../proposal-plan.md`, supervisor questions). Fallback: its values appear only in §2.5.
- Table size: 16 rows + group; could be cut to the ~10 rows with both σ and t₊.
- ¶6 (test conditions) dropped in the condensed §2.2 (14 Nov): §2.1 covers it; the DOD example (Sun, Kim) moved into §2.1. Also dropped from the proposal (kept in the long version): σ above bulk detail, σ–t₊ counts, Huang σ·t₊, soft shorts, high-DOD tests, Yuan's Na₂SO₄ HER test. **Moved to §2.3:** Debye length ≈ 0.1 nm at 2 M vs µm GF pores (charged pores).
- Claude's task while building the table: check the electrolyte per row (Gu's grade tests; the GF-life comparison in ¶5 assumes 2 M ZnSO₄ throughout).
- Decided 12 Nov: BV only as a one-sentence limitation here, the discussion in §4/§5. Proposed: Sand's time as one sentence in ¶1; t₊ thread (section header).
- `review-matrix.md` §2.2 synthesis still calls the group's 3738 h "typical, not exceptional" — conflicts with the 12 Nov wording decision; reword there?
- Years in the matrix labels differ from Zotero for 6 items (e.g. "Cha 2025" = `cha_stable_2024`, "Yang 2022" = `yang_situ_2021`); the text uses the bib year.
