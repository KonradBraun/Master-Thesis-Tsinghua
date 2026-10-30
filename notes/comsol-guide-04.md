# COMSOL Modell 04: Virtueller Bruce–Vincent-Versuch (1D)

Stand 30.10. (Einstellungen per Screenshot aus Modell 03 bestätigt, S6-Rohdaten ausgewertet). Basis: `04_ZnZn_1D_BruceVincent.mph` (= Save As von 03, nur Parameter `dV = 10[mV]` ergänzt; gespeicherte Lösung ist noch die alte aus 03). ⚠️ = Menüname nicht sicher.

## Ziel
Die Gruppe misst t₊ mit Bruce–Vincent (ΔV = 10 mV laut SI, 600 s): GF 0.51, ND@GF 0.69. Wir machen denselben Versuch im Modell, gleiche Formel:

  t₊ = I_ss·(ΔV − η₀) / [I₀·(ΔV − η_ss)],  η = |η₁| + |η₂| (Durchtrittsüberspannung beider Elektroden)

1. **Check:** X = 0 liefert den Eingabewert t₊ = 0.51 → Methode funktioniert.
2. **Kern:** Wie weit kann eine 40-µm-ND-Schicht das *gemessene* t₊ der Zelle überhaupt anheben?
3. **Methodenkritik:** Wie stark verfälschen 600 s Messdauer und großes R_ct das Ergebnis — und wie groß ist der Stromabfall, den Ionentransport allein erzeugen kann?

## Was die S6-Rohdaten zeigen (eigene Auswertung 30.10., Details in `progress.md`)
- Ohm passt nicht zu 10 mV: I·R_gesamt ≈ 47–51 mV (GF), ≈ 14–16 mV (ND@GF).
- Nachgerechnet: GF t₊ = 0.52–0.53 (gemeldet 0.51); ND@GF **0.99–1.15** je nach EIS-Ablesung (gemeldet 0.69) → schlecht konditioniert, 0.69 nicht reproduzierbar → **kein Kalibrierziel**.
- Stromabfall gemessen −42 % (GF) / −13 % (ND@GF); Transport allein (gemessenes R_bulk) erklärt nur 0.5–4 % → der Abfall kommt von der Grenzfläche.
→ Modell 04 wird damit vor allem **Methodenkritik + Obergrenze für den Schichteffekt**; die Kalibrierung von X auf 0.69 entfällt (Vorschlag, noch nicht beschlossen).

## Erwartung (eigene Abschätzung — das Modell prüft sie)
- **Dünne Schicht hebt t₊ kaum:** R₀ = R_GF + R_ND, R_ss = R_GF/t₊,GF + R_ND/t₊,ND, gemessen t₊ ≈ R₀/R_ss. Mit R_ND/R_GF ≈ 0.065 und t₊,GF = 0.51 gibt selbst eine perfekt selektive Schicht nur **≈ 0.53**.
- **600 s:** Diffusionszeitkonstante L²/(π²·D_eff) ≈ 280 s (675 µm) → bei 600 s noch nicht ganz stationär, t₊ erscheint etwas zu hoch.
- **Kinetik:** i₀ = 5 A/m² → η₀ ≈ 9.87 von 10 mV, ΔV − η₀ ≈ 0.13 mV → hochempfindlich. Bei i₀ = 0.5 A/m² (≈ gemessenes R₀ der GF-Zelle, ~675 Ω) noch 10× schlimmer. i₀ = 2000 A/m² (UME-Wert, Rana et al.) = gut konditionierter Referenzfall.

## 0. Datei
Modell **03 ohne Speichern schließen**, **04** öffnen. Alles Folgende in 04, Studie = **Study 2** (Parametric Sweep + Time Dependent).

## 1. Randbedingung: Spannung statt Strom
- **Electrode Surface 1** (x = 0, ND-Seite): steht schon auf *Electric potential*, φ_s,ext = `0[V]` — passt, nichts ändern.
- **Electrode Surface 2** (x = L): *Electrode Phase Potential Condition* von **Average current density** auf **Electric potential**, φ_s,ext = **`dV`**.

## 2. Kinetik — bestätigt, nichts ändern
Electrode Reaction: E_eq = *Nernst equation* (E_eq,ref = 0 V), *Butler–Volmer*, *Mass action law*, i₀,ref = `i0`, α_a = 1, n = 2, ν_cZn = −1, ν_cX = 0. → COMSOLs η ist reine Durchtrittsüberspannung, genau was die Formel braucht.

## 3. Study 2
1. **Step 1: Time Dependent → Output times:** `0 10^range(-3,0.1,2.7) 600 10^range(2.8,0.1,3.6)` (bis ~4000 s; 0.1 s und 600 s wie in der Messung enthalten)
2. Gleicher Knoten: **Tolerance: User controlled → Relative tolerance `1e-6`** ⚠️
3. **Parametric Sweep** (*All combinations*): Zeile `i_app` löschen. Neu:
   - `X_ND` = `0 100 1000 3100 10000` (mol/m³; 10000 = Grenzfall fast perfekt selektiv)
   - `i0` = `0.5 5 2000` (A/m²)
   → 15 Rechnungen, eher Minuten als Sekunden.
4. **Speichern, dann Compute.** Falls X = 10000 oder i₀ = 0.5 nicht konvergiert: Wert weglassen, Rest reicht.

## 4. Auswertung — exportieren, rechnen mache ich
**a) Kurzer Blick:** *1D Plot Group → Point Graph*, Punkt 3, Ausdruck = Elektrolytstromdichte (Picker: tcd → *Electrolyte current density*, x-Komponente; vermutlich `tcd.Ilx` ⚠️), x-Achse log.

**b) Zwei Point Evaluations** (*Derived Values → Point Evaluation*), Datensatz = Parametric Solutions von Study 2, *Time selection: All*:
| Auswertung | Punkt | Ausdrücke |
|---|---|---|
| P1 | 1 (x = 0) | `phil`, `cZn` |
| P3 | 3 (x = L) | `phil`, `cZn`, Elektrolytstromdichte (wie a) |

η brauchst du nicht: ΔV − η₁ − η₂ = [φ_l(L) − φ_l(0)] + (RT/2F)·ln[c_Zn(L)/c_Zn(0)] (folgt aus der Nernst-Einstellung oben) — das rechne ich aus `phil` und `cZn`, genauer als die Differenz zweier fast gleicher Zahlen.

**c) Export:** beide Tabellen → *Export* → `COMSOL/results/04_BV_P1.csv` und `04_BV_P3.csv` (Ordner anlegen; CSVs kommen ins Git). Dann Bescheid geben → ich rechne t₊ (stationär + 600 s), plotte Modell gegen Messung und trage alles ein.

## 5. Checks vor dem Export
1. Stationär: Strom bei ~3160 s und ~3980 s praktisch gleich (< 0.1 %).
2. X = 0, i₀ = 2000: I_ss/I₀ ≈ 0.55 (nahe 0.51; Rest = kleine Kinetik-Korrektur).
3. I₀ bei X = 0 (eigene Abschätzung): i₀ = 2000 → ~120 A/m²; i₀ = 5 → ~1.9 A/m²; i₀ = 0.5 → ~0.19 A/m² (≈ 15 µA auf 0.785 cm² — zum Vergleich gemessen 68 µA GF bzw. 40 µA ND@GF, was wieder zu ~47 bzw. ~15 mV statt 10 mV passt).

## Optional danach
- **ND im ganzen GF:** Sweep `L_ND` = `40[um] 300[um] 600[um]` bei i₀ = 2000, X = 3100 → wie dick müsste die Schicht für 0.69 sein?
- Danach: i₀-Kalibrierung an Fig. 3c/3d (Anleitung folgt).
