# Thesis Proposal — Plan (4 Nov 2026)

**Deadline: Mon 14 Dec 2026** (student, 4 Nov). Template: ThuThesis 选题报告, English (18 Oct).
Thesis chapter outline (incl. full fundamentals): `outline.md`.

## Formal requirements — Tsinghua form V202401 (received 4 Nov; Word file in the repo root)
- Report ≥ 3000 words (≈ 7–8 pages of plain text, estimate). This is a minimum; the expected length is unknown.
- Must contain (not limited to): significance · literature review · objectives · expected outcomes · research plan · methodology · **key difficulties and proposed solutions** · overall schedule · **expected defence time**.
- Literature review: **Chinese and international literature**; *synthesise and analyse* results and trends — not a compilation. The form asks for approx. counts of each and a list of major references.
- Grade: written report 60 % (supervisor) + **oral presentation and defence 40 %** (examination committee).
- No separate fundamentals chapter required → fundamentals only as far as needed for the gap, woven into the review; the full fundamentals come later in the thesis.

## Proposed structure (4 Nov, not yet agreed) — pages are estimates, total ~25 p until calibrated
Replaces chapter cut (a) of 30 Oct for the **proposal**; cut (a) stays for the thesis (`outline.md`).

| § | Content | ~p | → thesis |
|---|---|---|---|
| 1 | **Background and significance** — grid storage, limits of Li-ion, AZIBs | 2–3 | Ch. 1 |
| 2 | **Literature review** (core) | 12–15 | SotA chapter, extended |
| 2.1 | AZIBs and the Zn anode problem: failure modes and how they feed each other (Zn ≈ Li-*metal* analogue) | | |
| 2.2 | Separators for Zn anodes: requirements, GF standard and its deficits, modification strategies → trends + **comparison table**; t₊, Sand's time, Donnan briefly where needed | | |
| 2.3 | Nanodiamonds and carbon nanomaterials in Zn batteries | | |
| 2.4 | Simulation of Zn deposition and separators: continuum/FEM, charged layers, phase field; atomistic only as context | | |
| 2.5 | Summary of trends and the research gap (group model: NDs as "hollow circles", SI §1.7) | | |
| 3 | **Objectives, research content, expected outcomes** — research question still open | 2 | Ch. 1 / gap |
| 4 | **Methodology and research plan** — model chain, governing equations actually used, BCs, calibration/validation, **preliminary results (models 01–04)**, parameter table (`../notes/parameters.md`) | 5–6 | methods chapter, extended |
| 5 | **Key difficulties and proposed solutions** — e.g. parameter uncertainty → sensitivity/UQ; t₊ unusable as target → virtual Bruce–Vincent; single cells without repeats; 2D pore geometry from SEM; 2 M ZnSO₄ non-ideal → Concentrated Electrolyte Transport | 1–2 | — |
| 6 | **Schedule and expected defence time** — Gantt, milestones | 1–2 | — |
| | References — count Chinese vs international | | |

LaTeX headings in `proposal/data/chap0*.tex` still follow `outline.md` → adapt once the structure is agreed.

## Word form — fields to fill (submitted with the report)
- [ ] Cover: name, student ID, department, discipline, supervisor + title, enrolment date
- [ ] Thesis title, date of the proposal report
- [ ] Interdisciplinary supervision yes/no (ask supervisor)
- [ ] Literature counts (Chinese / international) + major references
- [ ] Available research conditions: COMSOL 6.3 full licence (laptop), 5.6 (office), group data
- [ ] Experimental safety: no experiments → (1) No; (2)/(3) clarify whether still required
- [ ] Project category (ask supervisor) · thesis type: likely *applied fundamental research* (proposal)
- [ ] Main contents and schedule; completion dates: literature review + planning / research work / thesis writing

## Timeline — proposed 4 Nov, replaces the 30 Oct plan (§ numbers = structure above)
As of 4 Nov: no chapter text yet. Main effort: the literature review (reading and comparing, not writing). Preliminary results = models 01–04; 2D is optional for the proposal.
- **4 – 10 Nov:** model 04 ✅ (9 Nov) · literature search: reviews, set up literature matrices (separators, simulation studies)
- **11 – 17 Nov:** read + write §2.2 separators, §2.3 NDs · supervisor meeting (research question, length, form questions)
- **18 – 24 Nov:** §2.4 simulation, §2.1, §2.5 gap · §4 methodology with preliminary results · first 2D step (group geometry, models A/B) only if on track
- **25 – 29 Nov:** §1, 3, 5, 6 → full draft to supervisor ~29 Nov
- **30 Nov – 14 Dec:** revision · Word form · slides for the oral presentation (date unknown) · buffer · submission

Moved after the draft (optional for the proposal): i₀ calibration · verify group model in COMSOL.

## Questions for the supervisor
- [ ] Expected length? (form: ≥ 3000 words minimum)
- [ ] "Chinese literature": Chinese-language papers or work by Chinese groups? Expected counts?
- [ ] Date and length of the oral presentation; project category and thesis type for the form; interdisciplinary supervision needed?
- [ ] Citation style? Example proposals from previous students?
- [ ] Depth on simulation fundamentals vs electrochemistry?
- [ ] One committed scope, or alternatives with a recommendation?
- [ ] Her view on: the approach (mechanism ranking, `../notes/progress.md`) · dendrite growth in scope · manufacturing-chapter idea
- [ ] Which institution's rules apply — also RWTH? (no RWTH supervisor yet)
- [x] Template: ThuThesis 选题报告 (18 Oct) · content and grading: form V202401 (4 Nov)
- [x] Critique of the group's paper only through own simulation results (student, 30 Oct)
- [x] AI use: allowed, no declaration needed (student, 30 Oct)
