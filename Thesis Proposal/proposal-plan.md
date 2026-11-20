# Thesis Proposal — Plan (4 Nov 2026)

**Deadline: Mon 14 Dec 2026** (student, 4 Nov). Template: ThuThesis 选题报告, English (18 Oct).
**Submission package (WeChat group, 12 Nov) — all by 14 Dec:** (1) written proposal following the thesis template · (2) the form (= V202401 below), filled in and **signed by the supervisor**; signature fields for institutional director and committee stay empty · (3) PPT slides. **Oral defence ~17 Dec** (3rd week, session for Aachen students): 5–10 min talk + Q&A; time slots announced later.
Official Tsinghua thesis-template page (May 2026 guide, CN/EN Word templates) links the TUNA LaTeX template = ThuThesis; our v7.7.1 is synced to that guide edition.
Thesis chapter outline (incl. full fundamentals): `outline.md`.

## Formal requirements — Tsinghua form V202401 (received 4 Nov; Word file in the repo root)
- Report ≥ 3000 words (≈ 7–8 pages of plain text, estimate). This is a minimum; the supervisor finds the length not very critical (WeChat, relayed 19 Nov).
- Must contain (not limited to): significance · literature review · objectives · expected outcomes · research plan · methodology · **key difficulties and proposed solutions** · overall schedule · **expected defence time**.
- Literature review: **Chinese and international literature**; *synthesise and analyse* results and trends — not a compilation. The form asks for approx. counts of each and a list of major references. Decided (student, 10 Nov): "Chinese literature" = work by groups in China (easily met in this field; optionally 1–2 papers from Chinese journals); counts in `../Literature/review-matrix.md` ("CN vs international").
- Grade: written report 60 % (supervisor) + **oral presentation and defence 40 %** (examination committee).
- No separate fundamentals chapter required → fundamentals only as far as needed for the gap, woven into the review; the full fundamentals come later in the thesis.

## Proposed structure (4 Nov; §2 order agreed 12 Nov; length not critical, ~20–40 p as rough reference, student 20 Nov)
**Length (student, 20 Nov):** not critical (supervisor, WeChat, relayed 19 Nov) — ~20–40 pages of main text only as a rough reference, not a target; sections may grow where the content needs it; the proposal still carries the argument to the gap, detail goes to the thesis. Section split of the original ~20 p budget (14 Nov), now a lower bound: §1 ~1.5 · §2 ~7–8 (§2.1 1.5 · §2.2 2 + table · §2.3 1.5 · §2.4 1 · §2.5 0.75 · §2.6 0.5) · §3 ~2 · §4 ~5 · §5 + §6 ~2.
Funnel (student, 12 Nov): general → very specific → what this work does differently → research question. Simulation literature sits at separator level (§2.3), so §2 narrows without widening again; the group's work gets its own section (§2.5).

| § | Content | ~p | → thesis |
|---|---|---|---|
| 1 | **Background and significance** — grid storage, limits of Li-ion, AZIBs; why mechanistic understanding matters (rational separator design instead of trial and error) | ~1.5 | Ch. 1 |
| 2 | **Literature review** (core) | ~7–8 | SotA chapter, extended |
| 2.1 | AZIBs and the Zn anode problem: failure modes and how they couple through the interfacial pH; test conditions | | |
| 2.2 | Separators for Zn anodes: requirements, GF standard and its deficits, modification strategies → trends + **comparison table**; t₊, Sand's time, Donnan briefly where needed | | |
| 2.3 | Simulation of Zn deposition and separators: continuum/FEM, charged layers and pores, phase field; FEM practice in Zn separator papers; atomistic only as context | | |
| 2.4 | Nanodiamonds in Zn batteries: claimed roles, ND surface chemistry in 2 M ZnSO₄, ND@GF precedent (Zhang 2024) | | |
| 2.5 | Starting point — the group's ND@GF separator: improvement under identical conditions, proposed mechanisms, existing model (NDs as "hollow circles", 0.5 V, SI §1.7); neutral; only place where papers are discussed by name | ~1 | |
| 2.6 | Research gap and what this work does differently (operating point 2 mA cm⁻², NDs with physical properties, kinetics + concentration, quantitative metrics, mesh study, comparison with measurements, mechanism ranking) | | |
| 3 | **Objectives, research content, expected outcomes** — opens with a short preview of the preliminary findings (→ §4) that motivates the question; research question still open | 2 | Ch. 1 / gap |
| 4 | **Methodology and research plan** — model chain, governing equations actually used, BCs, calibration/validation, **preliminary results (models 01–05)**, parameter table (`../notes/parameters.md`) | ~5 | methods chapter, extended |
| 5 | **Key difficulties and proposed solutions** — e.g. parameter uncertainty → sensitivity/UQ; t₊ unusable as target → virtual Bruce–Vincent; single cells without repeats; 2D pore geometry from SEM; 2 M ZnSO₄ non-ideal → Concentrated Electrolyte Transport | ~1 | — |
| 6 | **Schedule and expected defence time** — Gantt, milestones | ~1 | — |
| | References — count Chinese vs international | | |

LaTeX chapters `proposal/data/chap01–06.tex` follow this structure (13 Nov); §2 prose: roadmap + §2.1 written 13 Nov (sources for the 3 "[source?]" markers found 14 Nov), §2.2 + Table 2.1 written 14 Nov and condensed to ~2 p + table (budget), §2.3 written 14 Nov (~1.4 p); all re-audited against full texts 14 Nov; §2.1 and §2.2 reviewed by the student and revised 16 Nov, §2.3 not yet reviewed; §2.4 written and audited against full texts 19 Nov (~1.3 p, not yet reviewed); §2.5 and §2.6 only as plans (comments in `chap02.tex`). Literature behind §2 re-audited 19 Nov; primary sources added where verified 20 Nov (open ones: download list in `../Literature/lit-review-todo.md`). Chapter 3: draft 13 Nov, first comments applied 14 Nov; stays in `main.tex` but is not final (open to change).

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
Preliminary results = models 01–05 (done by 10 Nov); 2D is optional for the proposal.
- **11 – 19 Nov ✅:** literature search and matrix · §2.1–§2.4 written (13–19 Nov) · WeChat update to the supervisor (reply relayed 19 Nov)
- **20 – 24 Nov:** §2.5 starting point, §2.6 gap · §4 methodology with preliminary results · first 2D step (group geometry, models A/B) only if on track
- **25 – 29 Nov:** §1, 3, 5, 6 → full draft to supervisor ~29 Nov
- **30 Nov – 14 Dec:** short chat with the supervisor (Thu 3 Dec afternoon, to confirm) · revision · Word form · slides for the oral presentation (5–10 min, defence ~17 Dec) · rehearsal with Dr Zhang (offered by the supervisor) · supervisor signature on the form before 14 Dec · buffer · submission

Moved after the draft (optional for the proposal): i₀ calibration · first 2D step. (Group model verified and re-run = model 05, 10 Nov.)

## Questions for the supervisor
Open questions go to the short chat in her Thursday afternoon discussion session (student away 26 Nov, proposing 3 Dec, to confirm).
- [ ] Project category and thesis type for the form; interdisciplinary supervision needed?
- [ ] Citation style? Example proposals from previous students?
- [ ] OK to cite the group's ND@GF manuscript (J. Power Sources, under review) in §2.5 as "manuscript under review"? Would she like the simulation results in a revision of that paper or in a follow-up paper?
- [ ] Depth on simulation fundamentals vs electrochemistry?
- [ ] One committed scope, or alternatives with a recommendation?
- [ ] Her view on: the approach (mechanism ranking, `../notes/progress.md`) · dendrite growth in scope · manufacturing-chapter idea
- [ ] Which institution's rules apply — also RWTH? (no RWTH supervisor yet)
Answered questions (length, "Chinese literature", defence date, template, AI use) are recorded above and in `../CLAUDE.md`; framing of the critique in `../notes/progress.md`.
