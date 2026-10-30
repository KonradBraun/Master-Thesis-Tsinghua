# COMSOL Modell 04: Virtueller Bruce–Vincent-Versuch (1D)

Stand 30.10. Basis: `04_ZnZn_1D_BruceVincent.mph` (= Save As von 03, nur Parameter `dV = 10[mV]` ergänzt; die gespeicherte Lösung ist noch die alte aus 03). Menüpunkte mit ⚠️ sind nicht sicher — im Zweifel per Picker suchen.

## Ziel
Die Gruppe misst t₊ mit Bruce–Vincent (ΔV = 10 mV, I_s nach 600 s, SI Fig. S6): GF 0.51, ND@GF 0.69. Wir machen denselben Versuch im Modell und rechnen mit derselben Formel:

  t₊ = I_ss·(ΔV − η₀) / [I₀·(ΔV − η_ss)],  η = |η₁| + |η₂| (Durchtrittsüberspannung beider Elektroden)

Drei Fragen:
1. **Check:** Liefert das Modell ohne ND-Ladung (X = 0) wieder den Eingabewert t₊ = 0.51? → Methode funktioniert.
2. **Kern:** Kann eine 40-µm-ND-Schicht mit Festladung X das *gemessene* t₊ der ganzen Zelle auf 0.69 heben — und mit welchem X?
3. **Protokoll:** Was ändert der Abbruch bei 600 s (wie bei der Gruppe) gegenüber dem echten stationären Zustand?

## Erwartung (eigene Abschätzung — das Modell prüft sie)
- **Dünne Schicht hebt t₊ kaum.** Bei t = 0 leiten beide Ionen, im stationären Zustand nur Zn²⁺. Jeder Bereich wirkt dann wie sein „Zn²⁺-Anteil-Widerstand": R₀ = R_GF + R_ND, R_ss = R_GF/t₊,GF + R_ND/t₊,ND, und der Versuch misst t₊ ≈ R₀/R_ss. Mit r = R_ND/R_GF ≈ (40/0.89)/(635/0.92) ≈ 0.065 und t₊,GF = 0.51 gibt selbst eine perfekt selektive Schicht (t₊,ND = 1) nur **≈ 0.53**. Für 0.69 bräuchte man r ≈ 1.1 — die Schicht müsste mehr Widerstand haben als das ganze GF, was der gemessenen σ-Zunahme (2.83 → 2.94 S/m) widerspricht.
- **600 s reichen evtl. nicht.** Diffusionszeitkonstante τ₁ = L²/(π²·D_eff), D_eff = ε/τ · D_salt ≈ 0.5 · 3.27e-10 m²/s → ~280 s bei 675 µm (~115 s bei komprimierten ~430 µm). Bei 600 s liegt der Strom noch über I_ss → t₊ erscheint grob ~0.55 statt 0.51.
- **Kinetik macht die Formel empfindlich.** Mit i₀ = 5 A/m² ist R_ct ≈ RT/(2F·i₀) ≈ 2.6e-3 Ω·m² pro Elektrode, der Elektrolyt im Modell nur ~7e-5 Ω·m² → η₀ ≈ 9.87 von 10 mV, ΔV − η₀ ≈ 0.13 mV. Ein Fehler von 0.01 mV in η verschiebt t₊ um ~8 %. In der echten Zelle (R_ct ~680 Ω vs. ~3 Ω Elektrolyt) ist das noch extremer → relevant für die Kritik F13/F19. Deshalb rechnen wir zusätzlich mit schneller Kinetik (i₀ = 2000 A/m², UME-Wert Rana et al., `parameters.md`): Dann dominiert der Elektrolyt und die Formel ist gut konditioniert.

## 1. Randbedingung: Spannung statt Strom
- **Electrode Surface 1** (Punkt 1, x = 0, Seite mit ND-Schicht): muss **Electric ground** sein — prüfen (in der Modellhistorie taucht auch „External short" auf).
- **Electrode Surface 2** (Punkt 3, x = L): Abschnitt *Electrode Phase Potential Condition* von **Average current density** (`i_app`) auf **Electric potential** umstellen, φ_s,ext = **`dV`** ⚠️ (Dropdown-Name).
→ ES2 liegt 10 mV höher: dort Auflösung, an x = 0 Abscheidung durch die ND-Schicht — wie in Modell 03.

## 2. Kinetik prüfen (wichtig für die Auswertung)
*Electrode Reaction* unter ES1 und ES2: Das Gleichgewichtspotential sollte **konzentrationsabhängig (Nernst, Reference concentrations = c0)** sein. Dann ist COMSOLs Überspannung η nur der Durchtrittsanteil — genau das, was die Formel abzieht. Steht dort ein konstantes E_eq (*User defined*), steckt die Konzentrationsüberspannung mit in η → bitte kurz melden, dann passe ich die Auswertung an.

## 3. Studie
1. **Time Dependent → Output times:** `0 10^range(-3,0.1,2.7) 600 10^range(2.8,0.1,3.6)`
   (logarithmisch bis ~4000 s ≈ 14 τ₁; 600 s extra für das Protokoll der Gruppe)
2. **Toleranz:** im selben Knoten *Study Settings → Tolerance: User controlled*, **Relative tolerance `1e-6`** ⚠️ — nötig wegen der 0.13-mV-Differenz oben.
3. **Parametric Sweep** (*All combinations*): Zeile `i_app` löschen (wird nicht mehr benutzt). Neu:
   - `X_ND` = `0 100 1000 3100 10000` (mol/m³; 10000 = fast perfekt selektive Schicht, Grenzfall)
   - `i0` = `5 2000` (A/m²; realistisch-effektiv vs. schnelle Kinetik)
   → 10 Rechnungen. Modell 03 brauchte 86 s für 20 Fälle; mit der strengeren Toleranz eher ein paar Minuten.
4. **Speichern, dann Compute.**

## 4. Auswertung — Tabellen exportieren, rechnen mache ich
**a) Kurzer Blick:** *1D Plot Group → Point Graph*, Punkt 3, Ausdruck `abs(tcd.Ilx)` ⚠️ (Picker: tcd → Electrolyte current density, x component), x-Achse logarithmisch. Eine Kurve pro Fall: Abfall von I₀ auf ein Plateau.

**b) Zwei Point Evaluations** (*Derived Values → Point Evaluation*), jeweils *Time selection: All*, alle Parameterwerte:
| Auswertung | Punkt | Ausdrücke |
|---|---|---|
| P1 | 1 (x = 0) | `phil`, `cZn`, η der Electrode Reaction an ES1 ⚠️ |
| P3 | 3 (x = L) | `phil`, `cZn`, `abs(tcd.Ilx)`, η der Electrode Reaction an ES2 ⚠️ |

η per Picker: tcd → Electrode kinetics → Overpotential (Name vermutlich `tcd.eta_er1` / `tcd.eta_er2`). Falls nicht auffindbar: weglassen — aus `phil` und `cZn` kann ich ΔV − η auch direkt berechnen (= Elektrolytabfall + Nernst-Term; sogar genauer, weil keine Differenz fast gleicher Zahlen).

**c) Export:** jede Tabelle → *Export* → `COMSOL/results/04_BV_P1.csv` und `04_BV_P3.csv` (Ordner anlegen; CSVs kommen ins Git). Dann sag Bescheid — ich berechne t₊ für alle Fälle (stationär und bei 600 s), mache die Plots und trage alles in `progress.md` ein.

## 5. Checks (vor dem Export)
1. **Stationär?** `abs(tcd.Ilx)` bei ~3160 s und ~3980 s praktisch gleich (< 0.1 %).
2. **X = 0, i₀ = 2000:** I_ss/I₀ ≈ 0.55 (nahe t₊ = 0.51; der Rest ist die kleine Kinetik-Korrektur, die die Formel herausrechnet).
3. **Größenordnung I₀ (X = 0):** i₀ = 5 → ~1.9 A/m² (≈ 0.19 mA/cm², kinetisch begrenzt); i₀ = 2000 → ~120 A/m² (Elektrolyt-begrenzt) — eigene Abschätzung aus R_ct und R_Elyt oben.
4. Konvergenzprobleme bei X = 10000 → diesen Wert weglassen, Rest reicht.

## Mit den S6-Rohdaten (sobald in `Literature/group-data/`)
Ändert am Modell-Setup nichts — Modell 04 kann sofort gerechnet werden. Die Rohdaten nutze ich für:
1. **Tatsächliches Protokoll:** angelegte Spannung (wirklich 10 mV?), Dauer, Zeitauflösung (welcher Punkt ist „I₀"?), EIS vor/nach.
2. **t₊ exakt nachrechnen** (statt abgelesener ~Werte) → F13 bestätigen oder widerlegen.
3. **Gemessenes I(t) gegen Modell legen:** Im Modell fällt der Strom durch Ionentransport bei i₀ = 5 nur um ~1 %; gemessen ~42 % (GF) bzw. ~13 % (ND@GF). Bestätigen die Rohdaten das, kommt der Abfall von der Grenzfläche (R₀ → R_s), nicht vom Transport (Abschätzung in `progress.md`).
4. Ggf. dritter `i0`-Wert, passend zum gemessenen R₀ (R₀ ~680 Ω → i₀ ~0.5 A/m², eigene Rechnung mit A = 0.785 cm²) — erst nach Rohdaten-Check.

## Optional danach
- **ND im ganzen GF statt nur oben:** zweiter Sweep `L_ND` = `40[um] 300[um] 600[um]` bei i₀ = 2000, X = 3100 → zeigt, wie dick die Schicht für 0.69 sein müsste (Gegenprobe zur Abschätzung oben).
- Danach: i₀-Kalibrierung an Fig. 3c/3d (Anleitung folgt).
