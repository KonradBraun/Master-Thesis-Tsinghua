# Literature review — to-do (proposal §1–§2)

Living list, carried over from the night loop of 10 Nov 2026. Results go into `review-matrix.md` (conventions in its header); Zotero tags and notes as described there. Strike or reorder freely.

## For the student — papers to download (updated 25 Nov)
Put the PDFs into `manual download/`; Claude then converts them (`bash tools/pdf2txt.sh "Literature/manual download"`), checks the values and switches the citations. All papers below are already in Zotero (metadata only). "OA" = free to read, but the publisher blocks automated download.

**A. Still needed for the proposal text (before 14 Dec)**
| Paper | DOI | Why |
|---|---|---|
| Yang 2024, Energy Environ. Sci. — **main text** (the file that arrived 25 Nov is only the SI) | `10.1039/d3ee04515c` | HER at low vs high current density (§2.2 comment, now via Rana AEM) |
| Ziegler 2019, Joule | `10.1016/j.joule.2019.06.012` | same cost target as Sepulveda (§1); Sepulveda alone is enough if this one stays missing |

**C. Low priority** (context, not cited): Guo 2025, Energy Environ. Sci. `10.1039/d4ee05044d`

**Arrived and checked 25 Nov** (rows and corrections in `review-matrix.md`, Zotero status tags updated)
- Kao 2023: HER faradaic efficiency 1.1 % for bare Zn‖Zn at 1 mA cm⁻², 0.5 mAh cm⁻² ✓ — but the electrolyte is **2 M** ZnSO₄ (Methods), not "2 m" as Rana AEM quotes and §2.1 l. 30 prints.
- Yang 2024 EES (SI only): Fig. S11b gives the H₂ **volume ratio of the sampled gas** (~60 / 32 / 7.5 / 2 % at 0.05 / 0.2 / 1 / 10 mA cm⁻²), not a faradaic HER share → the "HER share" wording in the chap02 comment (l. 95) is wrong.
- Fenta & Bouchal 2024: t_Zn 0.70 for 31 m ZnCl₂ (potentiostatic "steady-current method") ✓. Zhang 2020 Carbon Energy: ~0.2 for 30 m ZnCl₂ only as a conductivity ratio in Fig. 1B; method in its SI (not read) → keep Gomez Vazquez as the source of the "Bruce–Vincent, factor of three" statement (§2.2 l. 149).
- Yu 2024 JACS: supports §2.1 l. 33 directly (H₂O-rich interface during desolvation speeds up HER; in situ FTIR + MD, 1 and 4 M ZnSO₄).
- Sand 1901: original derivation (transport number, i√t bound) ✓ — can be cited for "Sand's time" (§2.2 l. 88).
- Sepulveda 2021: ≤ US$20 kWh⁻¹ ✓ (for long-duration storage; with sufficient efficiency and power cost).
- Re-checked rows: Telmasre 2025 ✓, Zhang 2018 JES (210 s wording corrected), Li 2022 CCL ("no validation" → compared only with earlier simulations), Chen 2026 ✓.
- Full text instead of abstract: Dunn 2011, Gao 2022, Kim 2024 (its Zn value 5845 mAh cm⁻³ is a typo-level mismatch with Dong's 5854; Dong's is consistent), Wu 2021 (> 550 h at 5 mA cm⁻², twice GF).

**D. Supporting information — only if the point becomes needed** (what each SI is for: "Needs access" lists in `review-matrix.md`)
Zhao 2024 CCL (OA) `10.1016/j.cclet.2023.109332` · Shao 2025 (OA) `10.1002/cey2.701` · Tan 2025 `10.1002/smll.202510596` · Zhang 2023 CEJ `10.1016/j.cej.2023.143312` · Luo 2024 `10.1016/j.cej.2023.148448` · Hansen 2023 `10.1016/j.memsci.2023.122130` · Akram 2025 `10.1016/j.matchemphys.2025.130863` · Liu 2024 AEM `10.1002/aenm.202401479` · Rana 2025 Joule `10.1016/j.joule.2025.102167`

**Other**
- Delete `manual download/d3ta06268f.pdf` (0 bytes; Lee 2024 JMCA is already there as "A hydrophilic Janus-faced separator with.pdf").
- Li 2024 Sci. Bull. is already in `manual download/` ("Separator designs…") — nothing to download, not read yet.
- Zn vs Li price (Cui 2025 quotes it from reviews; Kim 2024 gives metal prices Zn US$0.003 vs Li US$1.44 per g, also from its refs): decide whether a primary price source (e.g. USGS Mineral Commodity Summaries) is needed.
- Ask the group (WeChat, low priority): sp²/sp³/C–O/C=O fractions from the XPS fit behind Zhang 2026 ACS Nano Fig. 2D — only needed if ND surface chemistry becomes a model parameter.
- Done earlier: all downloads requested until 14 Nov arrived and were processed (Cha 2024, Zhang 2024 AEM, Zheng 2019, Blanc 2020, Tang 2019 and the 13 Nov batch).

## Status (25 Nov)
- Proposal §2 complete in `../Thesis Proposal/proposal/data/chap02.tex`, incl. Table 2.1; §2.5 (group's ND@GF work) and §2.6 (gap) written and audited 25 Nov, not yet reviewed.
- Literature work done: broad search (10–11 Nov), targeted round T1–T9 (13 Nov: simulation critique and V&V, HER/pH/ZHS models, charged pores, ND layer, §1 cost and safety sources, thermodynamic factor, CN/INT count, Chinese-language search), claim-by-claim audit of `review-matrix.md` and `notes/parameters.md` against the full texts (19 Nov). Results live in the matrix.
- Further searches only as targeted gaps right before the section that needs them.

## Open tasks
- [x] **Citation switches in chap02 from the 25 Nov downloads** (done 25 Nov, student's OK): §2.1 cites Kao 2023 (2 m → 2 M) and Yu 2024 (next to Xu 2023); §2.2 cites Sand 1901 for "Sand's time"; source comments updated; Table 2.1 caption now says "unless marked otherwise" (Yuan values from the SI). Zotero `use-*`: Kao `use-core`, Yu `use-drop` → `use-context`, Sand `use-context`.
- [ ] **`use-*` tags — student's decision:** the "Proposed `use-*`" lines in matrix §1, §2.2 (alternatives to GF), §2.3 and §2.4, plus Rana 2025 AEM (proposed `use-core`); most of these Zotero items have no `use-*` tag yet.
- [ ] **PDF processing (ongoing).** New files in `manual download/` → `bash tools/pdf2txt.sh "Literature/manual download"`; check for "Figure S1" captions before assuming an SI is included. Per paper: matrix row (incl. comparison-table fields: GF grade, Zn thickness → DOD, σ/t₊ with method and ΔV, Zn//Zn life at j/Q with GF control, CE, simulation setup), Zotero tag + note. Processed: everything in the folder as of 25 Nov.
- [ ] **Table 2.1:** group row waits for the supervisor's OK; whether life/DOD columns are added is open. Yang 2022 and Gou 2025 not added (student, 19 Nov: table detailed enough).
- [ ] **Alternatives to GF (optional):** subsection in matrix §2.2 (Zhou 2022, Zheng 2023, reviews Nian 2025 and Lee 2025); unverified further leads: 10.1002/adfm.202316619, 10.1002/aenm.202101299, 10.1063/5.0214281.
- [ ] **Consistency check:** `parameters.md` audited 19 Nov; `paper-summary.md` against the corrected matrix still open.
- [ ] **σ–t₊ figure** (GF → modified, full-text rows), optional.

## For the thesis — PDFs in `Potential/` not used yet (moved from `triage.md`, 20 Nov)
Papers from the student's PDF collection that the proposal does not use yet; text versions in `Potential/txt/`, Zotero tag `pdf-folder-import`. Chapter numbers refer to `../Thesis Proposal/outline.md`.
| Topic → thesis chapter | Files in `Potential/` |
|---|---|
| Sand's time (3.4) | MODIFICATION TO THE SAND'S APPROACH (PhD thesis, Akolkar group) |
| Donnan / charged membranes (4.6) | Comparative Analysis of Donnan Steric Partitioning … (Saavedra 2024) |
| ND synthesis, coal context (3.6) | Upgrading carbonaceous materials (Zang 2022, review) |
| Continuum models of Zn deposition (5.1) | NONISOTHERMAL SIMULATION OF (Zn in ZnSO₄, FEM + KMC) |
| Phase-field history (4.7, 5.3 — only if in scope) | Computer Simulation of Dendritic (Voss 1985) |
| V&V (4.8) | Verification and validation in computational (Babuška & Oden 2004) · Concepts of Model Verification and Validation (LANL report) · VER IF ICAT ION AND VAL IDAT ION IN (Oberkampf & Roy — **only the book's front matter**; get chapters if the V&V chapter needs them) |
| Cathode (2.4) | Recent Advances … Manganese Dioxide · Rechargeable Zn–MnO2 Batteries |
| Manufacturing chapter (option) | Continuous Roll-To-Roll Coating and Drying of (separators, TUM) · Scalable aqueous-phase fabrication of rGO (R2R vs vacuum filtration) · A facile method to enhance the uniformity and adhesion … · Enhancing Li-Ion Battery Performance with Alumina-Coated Separators · Fabrication Techniques for Graphene Oxide-Based Membranes |

### Not needed (off-topic, judged from the abstract)
Two-dimensional quantum-sheet films (MoS₂) · Electronic, Structural, and Magnetic Upgrading of Coal-Based Products · Bimetallic MOF glass fiber (Li–S) · Current density driven texture evolution in zinc powder anodes · Multifunctional pH-Controlling Electrolyte · The magnetohydrodynamic effect (alkaline) · Flexible electrodes review · Scalable Manufacturing of (MXene films) · Validating Computational Models (social-science models) · Transverse Number Measurement (scanned notes, no text)

Full-text access routes and blocked publishers: `../notes/claude-notes.md`.
