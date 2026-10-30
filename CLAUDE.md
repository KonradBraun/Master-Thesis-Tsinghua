# Master's Thesis — Project Context

## Setup
- Double master's: Tsinghua (host, Dept. of Mechanical Engineering, supervisor Xining Zang — she) + RWTH Aachen (home: Produktionstechnik / production engineering, specialisation Automatisierungstechnik / automation engineering). The thesis should fit the RWTH programme at least loosely.
- Thesis in English, written in LaTeX.
- Topic: simulating the influence of nanodiamonds in a glass fibre separator for aqueous zinc-ion half and full cells.

## Working rules
- **Answers short and to the point**, coding-assistant style: lead with the answer, no padding. Go into detail only for genuinely new topics or when asked.
- **Language:** chat in English; German for detailed explanations of topics new to the student, with English technical terms alongside.
- **Background:** strong on Li-ion, new to zinc-ion. Knows continuum FEM/CFD (Moldex3D) — explain electrochemistry and Zn-specific concepts; the FEM workflow can be assumed familiar.
- **.md files must stay current** — outdated content misleads future sessions. Small factual updates (status, completed tasks, setup) are made right away and mentioned. Larger changes (plan, structure, decisions, deleting content) are proposed first and made after the student's OK — don't change prematurely. Ask when unsure whether something is decided. Keep files short; replace outdated content rather than appending.
- **Keep repo and notes lean** (student, 30 Oct): remove outdated, wrong or no-longer-needed content and files — Git keeps old versions. Routine cleanup (finished guides, done tasks, superseded numbers) right away and mention it; removing decisions or plan content still needs the OK. COMSOL step guides (`notes/comsol-guide-NN.md`) are temporary: once the model is done and its results and key setup are in `progress.md`, delete the guide.
- **Literature comes from Zotero, never from memory.** Author names, titles, DOIs and BibTeX via the Zotero MCP server (Zotero must be running). Missing sources are added to Zotero first, by DOI. Never expand author initials.
- **Every number needs a source:** paper/SI with figure or table, a Zotero reference, or an explicit "estimate". Values read off figures are marked "~".
- **Verify before recommending** tools, plugins, repos or licences (requirements, maintenance, compatibility). Flag anything unverified as an inference.

## Status
**Decided (supervisor, 14 Oct 2026):** the simulation is done in COMSOL only — no DFT, because it is computationally expensive and transferring atomistic results to the continuum model isn't realistic in the time available. First task: get familiar with COMSOL.

**Decided (18 Oct):** proposal in Tsinghua format (ThuThesis 选题报告), English.

**Proposal deadline:** mid-December 2026 (student, 30 Oct). **Thesis deadline:** ~15 Jul 2027 (student, unconfirmed); aim to finish late Jun / early Jul. **RWTH supervisor:** none yet (30 Oct). **AI use:** allowed, no declaration needed (student, 30 Oct).

**Not yet decided:** research question, exact scope (e.g. whether dendrite growth is simulated), proposal length. Earlier suggestions on these are proposals, not decisions.

**Starting point:** the group's existing COMSOL model represents the nanodiamonds as "hollow circles" with no specified surface properties (SI §1.7).

**COMSOL:** version 6.3 runs on the laptop this project runs on. The office PC has **5.6** (cannot open 6.3 files; GUI differs, e.g. no separate Species Charges node — charges probably in the Electrolyte node, unverified). Full licence — includes Electrochemistry, Electrodeposition, Battery Design, Corrosion, Optimization and Uncertainty Quantification.

## Key files
- `notes/progress.md` — current state, proposed plan (not agreed), setup, pending tasks
- `Literature/paper-summary.md` — group paper + SI: methods, measured data, critical findings
- `notes/comsol-guide-NN.md` — temporary step-by-step guide for the COMSOL model currently being built
- `notes/parameters.md` — model parameter table with sources and status (living file, becomes proposal §7.5)
- `Literature/triage.md` — triage of the student's PDF collection (`Literature/Potential/`, text versions in `txt/`) and open literature gaps
- `Thesis Proposal/proposal/` — the proposal in LaTeX (ThuThesis v7.7.1, Tsinghua 选题报告 format, English, XeLaTeX); `ref/refs.bib` from Zotero via `tools/zotero2bib.ps1` (PowerShell; `bash` in PowerShell hits WSL) or `tools/zotero2bib.sh` (Git Bash)
- `Thesis Proposal/outline.md` — draft proposal structure without DFT, open options, questions on formalities, literature workflow
- `Reference/` — background primers (German)
- `notes/claude-notes.md` — Claude's own short notes on pitfalls and non-obvious facts; read before relying on assumptions
