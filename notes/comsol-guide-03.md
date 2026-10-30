# COMSOL Modell 03: ND-Schicht mit fester Ladung (1D)

Stand 19.10. Baut auf `02_ZnZn_1D_separator.mph` auf (COMSOL 6.3, Laptop). Menüpunkte sind aus 6.3-Erfahrung mit 01/02 abgeleitet; was ich nicht sicher weiß, ist mit ⚠️ markiert.

## Ziel und Idee
Bisher: nur GF. Jetzt kommt zwischen Anode und GF eine dünne **ND-Schicht mit negativer Festladung** dazu. Das ist der im Paper behauptete Mechanismus (O-terminierte ND-Oberfläche stößt SO₄²⁻ ab, zieht Zn²⁺ an).

Physik (Teorell–Meyer–Sievers / Donnan-Modell): Die Festladung wird über das Porenvolumen „verschmiert" als Konzentration `X` (mol/m³). Elektroneutralität in der Schicht wird dann zu

  2·cZn − 2·cSO4 − X = 0

→ in der Schicht ist mehr Zn²⁺ als SO₄²⁻, der Strom wird dort fast nur von Zn²⁺ getragen (lokal hohes t₊).

**Trick für COMSOL:** Die Festladung wird als **dritte Spezies `cX`** mit Ladung −1 und praktisch null Diffusion eingebaut. Sie bewegt sich nicht, reagiert nicht und geht trotzdem in die Elektroneutralität ein. Funktioniert ohne Spezial-Knoten.

`X` ist eine *effektive* Größe (Volumenmittel). Später Umrechnung in Oberflächenladung für den Plausibilitätscheck mit Zeta-Potential: X ≈ σ_s·a_s/(F·ε) (a_s = innere Oberfläche pro Volumen).

## 0. Neue Datei
`02_…` öffnen → **Save As** `COMSOL/03_ZnZn_1D_ND_layer.mph`.

## 1. Parameter (zusätzlich zu 02)
| Name | Expression | Description |
|---|---|---|
| `L_ND` | `40[um]` | group: 30–50 um (19 Oct) |
| `eps_ND` | `0.89` | own calc. from 0.1–0.4 mg ND (0.87–0.91) |
| `tau_ND` | `tau_sep` | ASSUMPTION: few vol% ND barely change tortuosity |
| `X_ND` | `0[mol/m^3]` | fixed charge conc., fitted later (0 = sanity check) |
| `D_X` | `1e-18[m^2/s]` | immobile fixed charge (numerical) |

## 2. Geometrie: zwei Bereiche
*Geometry → Interval 1*: Koordinaten **`0`, `L_ND`, `L`** (drei Zeilen; ggf. „Specify: Coordinates"). **Build All**. Gesamtdicke bleibt `L`: die NDs sitzen laut Gruppe *auf den Fasern* der obersten 30–50 µm, keine zusätzliche Schicht.
→ 2 Domänen (1 = ND-Schicht an der Anode, 2 = GF), 3 Randpunkte.

⚠️ **Electrode Surface 2 muss danach auf Punkt 3** (rechts) stehen, nicht Punkt 2 (das ist jetzt die innere Grenze). Prüfen!

## 3. Dritte Spezies
*tcd* anklicken → Abschnitt **Dependent Variables**: Anzahl Spezies auf **3**, neuer Name **`cX`**.
⚠️ Falls sich die Anzahl dort nicht ändern lässt: neues Modell per Wizard mit 3 Spezies (`cZn`, `cSO4`, `cX`) und die Parameter per Copy/Paste übernehmen.

Im selben Fenster: **Species from electroneutrality** = **`cSO4`** (nicht cX!).

## 4. Physik-Knoten
- **Species Charges:** z_cZn = `2`, z_cSO4 = `-2`, z_cX = `-1`
- **Electrolyte 1, Separator 1 und Separator 2:** Diffusion cX = `D_X` (cZn, cSO4 wie gehabt)
- **Separator 1** (GF): Auswahl **nur Domäne 2**, `eps_sep`, Tortuosity `tau_sep`
- **Separator 2** (neu, Rechtsklick tcd → Separator): Auswahl **Domäne 1**, `eps_ND`, Tortuosity `tau_ND`
- **Initial Values 1:** Domäne 2: cZn = `c0`, cX = `0`
- **Initial Values 2** (neu, Rechtsklick tcd → Initial Values): Domäne 1: cZn = `X_ND/4 + sqrt(X_ND^2/16 + c0^2)`, cX = `X_ND`
  (= Donnan-Gleichgewicht mit 2 M im GF: cZn·cSO4 = c0², cZn − cSO4 = X/2. Mit cZn = c0 als Start fehlt in der Schicht Salz, das in der geschlossenen Zelle aus dem GF nachgezogen wird → ganzes GF-Profil sinkt bei hohem X ab — Artefakt, so am 19.10. beobachtet.)
- **Electrode Reactions (beide):** jetzt ist cSO4 die berechnete Spezies → Felder für cZn und cX erscheinen: **ν_cZn = `-1`, ν_cX = `0`** (ν_cSO4 ergibt sich zu 0). Reference concentrations: alle auf `c0` (nicht 0).

**Warum cX diffusionsfrei:** Über 30 min wandert es mit D = 1e-18 m²/s nur ~0,04 µm — bleibt also, wo es ist. D = 0 exakt kann den Löser singulär machen.

## 5. Netz
An der Grenze ND/GF springt die Ladung → steile Gradienten. Statt *Extremely fine*:
*Mesh 1* → Rechtsklick → **Distribution**: Domäne 1 → **200 Elemente**; zweite Distribution: Domäne 2 → **200 Elemente**, Element ratio ~10, symmetrisch. **Build All**.

## 6. Studie
*Study* (Time Dependent, `range(0,10,1800)`) + **Parametric Sweep** `X_ND` = `0 50 100 1000 3100` (0 = check; 50–100 = realistic upper bound from ND loading; 3100 = needed for local t₊ 0.69, see `parameters.md`) (Einheit: mol/m^3 — Spalte *Parameter unit*, oder leer lassen, da im Parameter definiert).

## 7. Prüfen
1. **Sanity check X_ND = 0:** Ergebnis ≈ Modell 02 (1895/2105 mol/m³). Kleine Abweichung nur durch die dichtere ND-Schicht. Wenn nicht → Fehler im Aufbau, erst beheben.
2. **cZn und cSO4 über x** (letzter Zeitpunkt), herangezoomt auf 0…30 µm: in der Schicht cZn > cSO4, Sprung an der Grenze (Donnan).
3. **Lokales t₊** als Line Graph: `D_Zn*cZn/(D_Zn*cZn+D_SO4*cSO4)` → in der Schicht deutlich > 0.51.
4. **cZn an der Anode (x = 0)** vs. X_ND — das ist die Kerngröße: wie viel Zn²⁺ steht der Abscheidung zur Verfügung.
5. Spannung `tcd.phis_es2`.

## Was zu erwarten ist (qualitativ, eigene Überlegung)
- Im **stationären** Zustand fließt SO₄²⁻ nirgends (es reagiert nicht). Das GF-Profil ändert sich durch eine dünne Schicht daher kaum. Der Effekt zeigt sich **an der Anodenoberfläche** (Donnan-„Puffer": mehr Zn²⁺ direkt an der Elektrode) und vor allem im **Zeitverlauf** und bei **hohen Strömen** (Sand-Zeit, Grenzstrom).
- Deshalb danach: Sweep über `i_app` (z. B. 2–20 mA/cm²) mit und ohne Ladung.

## Danach
- **Virtueller Bruce–Vincent / Kalibrierung an t₊ = 0.69:** Modell 04, eigene Anleitung `comsol-guide-04.md` (30.10.).
- Plausibilitätscheck X_ND ↔ Zeta-Potential / Oberflächenladung (Daten vom Postdoc).
- L_ND, eps_ND, tau_ND aus Postdoc-Daten (ND-Menge, Querschnitt-SEM) ersetzen.
