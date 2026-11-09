# COMSOL Modell 05: Nachrechnung Gruppenmodell (Varianten A und B)

Stand 9.11. Basis: die zwei Dateien vom Prof (`COMSOL/Old models/GF(1).mph`, `ND@GF(1).mph`) = vermutlich Fig. 2h/i. Inhalt laut Dateiauslese: `paper-summary.md` F5. ⚠️ = Menüname nicht sicher.

## Ziel
Die beiden Modelle unterscheiden sich in zwei Dingen: ND-Reihe (100 Löcher, isolierend; das Material „C (diamond)" ist keiner Domäne zugewiesen) **und** Separatorleitfähigkeit (2.15 → 0.5 S/m). Wir trennen das:

| Fall | Separator | ND-Reihe |
|---|---|---|
| GF (Original) | 2.15 S/m | — |
| ND@GF A (Original) | 0.5 S/m | ja |
| ND@GF B | 2.15 S/m | ja → unterscheidet sich von GF **nur** durch die ND |

**Metrik:** Verhältnis Maximum/Mittelwert des Feldes |E| an der Zinkoberfläche (im Elektrolyt ist E proportional zur Stromdichte) + Gesamtstrom. Absolute Feldbilder vergleichen wir nicht — das Modell ist linear, die Spannung skaliert nur.

## 0. Dateien
Originale nicht verändern: `GF(1).mph` öffnen → **Save As** `COMSOL/05_group_GF.mph`; `ND@GF(1).mph` → **Save As** `COMSOL/05_group_NDGF.mph`. Meldet COMSOL eine fehlende Lizenz oder deaktivierte Knoten → Bescheid geben.

## 1. Erst ansehen (5 min, beide Modelle) — kurz notieren
- *Geometry 1*: Längeneinheit (µm?)
- *Materials*: ZnSO4 [liquid] 3.5 S/m · SiO2 2.15 (GF) bzw. 0.5 (ND@GF) · C (diamond) ohne Zuweisung (Warnsymbol, harmlos)
- *Electric Currents*: Terminal 0.5 V und Ground — auf welchen Rändern?
- *Results*: Elektrisches Feld — sieht es aus wie Fig. 2h/i?

## 2. ND@GF: Separatorleitfähigkeit als Parameter
1. *Global Definitions → Parameters*: `sig_sep` = `0.5[S/m]`
2. *Materials → SiO2 (fused quartz)* → Electrical conductivity: `0.5` durch **`sig_sep`** ersetzen
3. *Study 1* → Rechtsklick → *Parametric Sweep*: `sig_sep` = `0.5 2.15 2.94` (Einheit S/m; 2.94 = gemessener Wert ND@GF, Fig. 2a)
4. Compute. Im GF-Modell genauso: Parameter `sig_sep` = `2.15[S/m]`, SiO2-Leitfähigkeit → `sig_sep`, Sweep `2.15 2.83` (2.83 = gemessener Wert GF).
   → drei Vergleiche: Original (2.15 vs 0.5) · gleich (2.15 vs 2.15) · gemessen (2.83 vs 2.94).

## 3. Auswertung (beide Modelle)
1. **Zinkoberfläche als Auswahl:** *Definitions → Selections → Explicit*, *Geometric entity level: Boundary*, alle Randstücke zwischen Zink und Elektrolyt anklicken (flache Stücke + Halbkreise), Label `Zn surface`.
2. *Derived Values →* **Line Maximum** und **Line Average**: Ausdruck `ec.normE`, Auswahl `Zn surface`.
   - Kommen Werte ≈ 0 heraus, wurde die Zinkseite ausgewertet → `up(ec.normE)` oder `down(ec.normE)` probieren (einer davon ist die Elektrolytseite).
3. *Derived Values → Global Evaluation*: Terminalstrom (Picker: ec → Terminal current; vermutlich `ec.I0_1` ⚠️).
4. Alle drei in **eine Tabelle** (ND@GF: beide `sig_sep`-Werte) → *Export* → `COMSOL/results/05_group_GF.txt` und `05_group_NDGF.txt`.
5. Optional zum Anschauen: *Line Graph* `ec.normE` auf `Zn surface`, x-Achse = x.

Fehlt in einer Tabelle ein Wert oder Fall → Datei neu exportieren.

## Erwartung (eigene Überlegung)
- A (Original) zeigt ein kleineres Max/Mittel als GF — so wie im Paper.
- Offen ist B: Bleibt der Unterschied, homogenisiert schon die bloße Partikelreihe (geometrischer Effekt → stützt die Porenstruktur-Richtung). Verschwindet er, kam er von der Separatorleitfähigkeit.
- Achtung bei der Deutung: Die ND-Reihe ist eine fast geschlossene Barriere (80 % der Breite blockiert, 0.4-µm-Schlitze). B testet also einen „Lochblech"-Effekt, nicht die echte ND-Struktur (~5-nm-Partikel verteilt über 30–50 µm).
- Der Terminalstrom zeigt, wie viel „weniger Strom" bei 0.5 S/m im Spiel ist.
