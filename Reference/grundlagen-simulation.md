# Grundlagen: Simulation — Einstieg für Anfänger

Erklärt von Null, mit Moldex3D als Anknüpfungspunkt. Englische Fachbegriffe in Klammern.

---

## 1. Warum überhaupt simulieren?

Ein Experiment sagt dir **dass** etwas passiert. Eine Simulation kann sagen **warum** — und was passieren würde, wenn man etwas ändert, das man experimentell gar nicht ändern kann.

Konkret für deine Arbeit:

| Frage | Experimentell | Simulativ |
|---|---|---|
| Funktioniert ND@GF besser als GF? | ✅ schon beantwortet | — |
| **Warum** funktioniert es besser? | Nur indirekt erschließbar | ✅ Kernstärke |
| Was passiert bei doppelter ND-Menge? | Neue Probe nötig | ✅ Parametervariation |
| Was, wenn die NDs ungleichmäßig verteilt sind? | Kaum kontrollierbar | ✅ frei einstellbar |
| Wie verhält sich die (100)-Fläche statt (111)? | **Nicht herstellbar** | ✅ einfach modellierbar |

Die letzte Zeile ist entscheidend: Man kann keinen Separator synthetisieren, der **ausschließlich** (100)-Flächen hat, um ihn mit einem zu vergleichen, der ausschließlich (111) hat. In der Simulation baut man einfach beides. **Deshalb ist Simulation der einzige ehrliche Weg zu der "general principle"-Behauptung des Papers.**

---

## 2. Die Längenskalen-Leiter

Das wichtigste Konzept überhaupt. Physikalische Vorgänge spielen auf sehr unterschiedlichen Größenordnungen, und **für jede Skala gibt es eigene Methoden**. Keine Methode deckt alle ab.

```
 10⁻¹⁰ m   Å      Elektronen, chemische Bindung        →  DFT
 10⁻⁹  m   nm     Atome in Bewegung, Hydrathülle       →  Molekulardynamik (MD)
 10⁻⁶  m   µm     Poren, Ionentransport, Dendriten     →  Kontinuum (FEM), Phase-Field
 10⁻³  m   mm     ganze Zelle, Spannungskurven         →  Zellmodell (P2D)
```

**Faustregel:** Je kleiner die Skala, desto genauer die Physik — und desto weniger Material kann man berechnen. DFT ist extrem genau, schafft aber nur ein paar hundert Atome. Ein Kontinuummodell rechnet mühelos einen ganzen Separator, weiß aber nicht, dass es Atome gibt.

Dein Problem liegt **über mehrere Skalen verteilt**: Die Ursache (Sauerstoff auf einer Diamantoberfläche) sitzt bei 10⁻¹⁰ m, die Wirkung (gleichmäßiger Ionenfluss im Separator) bei 10⁻⁶ m. Das ist genau die Lücke, die das Paper offen lässt.

---

## 3. Zwei Paradigmen

### Paradigma A — Kontinuum (dein Heimatgebiet)

Man tut so, als wäre Materie ein **glattes Kontinuum** ohne Atome. Man schreibt Erhaltungsgleichungen (Masse, Impuls, Ladung) als partielle Differentialgleichungen, zerlegt das Gebiet in ein Netz und löst numerisch.

Materialverhalten kommt als **Stoffwert von außen hinein** — Viskosität, Diffusionskoeffizient, Leitfähigkeit. Das Modell berechnet diese Werte nicht, es benutzt sie.

→ Moldex3D, COMSOL, Abaqus, Ansys

### Paradigma B — Atomistik (neu für dich)

Man modelliert **einzelne Atome**. Es gibt kein Netz und kein vorgegebenes Materialmodell — die Materialeigenschaften **entstehen aus der Rechnung**.

Statt Netzkonvergenz sorgt man sich hier um Basissatz-Konvergenz, Zellgröße und statistische Abtastung.

→ VASP, Quantum ESPRESSO, LAMMPS

### ⭐ Die Moldex3D-Brücke

Der Zusammenhang zwischen beiden wird sofort klar, wenn du an deine eigene Arbeit denkst:

In Moldex3D baust du Geometrie, vernetzt, weist **Materialdaten** zu, setzt Randbedingungen, löst, wertest aus.

**Woher kamen die Viskositätsdaten?**

Aus einem **Rheometer**. Jemand hat eine Probe gemessen. Moldex3D hat diese Daten *konsumiert*, nicht hergeleitet. Moldex3D weiß nicht einmal, dass Polymere aus Ketten bestehen — es braucht nur eine Zahl.

**Genau das ist das Verhältnis zwischen DFT und COMSOL:**

| Spritzguss | Batteriesimulation |
|---|---|
| Moldex3D simuliert das Bauteil | **COMSOL** simuliert die Zelle |
| Rheometer liefert Stoffwerte | **DFT** liefert Stoffwerte |
| Viskosität, PVT, Wärmeleitfähigkeit | Diffusionskoeffizient, Adsorptionsenergie, Reaktionsrate |
| Kennt keine Moleküle | Kennt keine Atome |

Einziger echter Unterschied: Das Rheometer **misst** physikalisch, DFT **berechnet** aus der Quantenmechanik. Die Rolle im Arbeitsablauf ist identisch — beide liefern die Materialeigenschaften, die die große Simulation braucht, aber selbst nicht herleiten kann.

---

## 4. Kontinuumssimulation (COMSOL)

### Was COMSOL ist

Allgemeine Multiphysik-FEM-Software. Moldex3D ist ein **Spezialwerkzeug**: nur Spritzguss, die Physik ist fest eingebaut und vor dir versteckt, die Gleichungen kannst du nicht ändern. COMSOL ist der **Generalist**: du wählst die Physik, siehst die Gleichungen, kannst sie ändern und mehrere Physiken koppeln.

Es gibt fertige Module — unter anderem ein **Battery Design Module**.

### Was in deiner Arbeit simuliert würde

**Gebiet:** der elektrolytgefüllte Raum zwischen Zinkanode und Kathode, also der Separatorbereich. Größenordnung: einige zehn bis hundert µm.

**Gesuchte Felder** (die Größen, die über Ort und Zeit variieren):
- **c(x,y,t)** — die Zn²⁺-Konzentration an jedem Punkt
- **φ(x,y,t)** — das elektrische Potential an jedem Punkt

**Die Gleichungen:**

*Nernst-Planck* — wie Ionen sich bewegen. Zwei Antriebe:

$$\mathbf{N} = \underbrace{-D\,\nabla c}_{\text{Diffusion}} \;\; \underbrace{-\, z\,u\,F\,c\,\nabla\phi}_{\text{Migration}}$$

**Diffusion:** Ionen wandern von hoch nach niedrig konzentriert — mathematisch dasselbe wie Wärmeleitung.
**Migration:** geladene Ionen werden vom elektrischen Feld geschoben. Das kennst du aus dem Spritzguss nicht, aber die Struktur der Transportgleichung ist dieselbe wie bei deinen Strömungsgleichungen.

*Butler-Volmer* — die Randbedingung an der Zinkoberfläche. Sie verknüpft, wie stark man treibt (Überspannung η), mit dem, wie schnell Zink abgeschieden wird (Stromdichte i):

$$i = i_0\left[\exp\!\left(\frac{\alpha_a F \eta}{RT}\right) - \exp\!\left(\frac{-\alpha_c F \eta}{RT}\right)\right]$$

Der wichtige Term ist **i₀, die Austauschstromdichte** — im Grunde "wie leicht läuft diese Reaktion". In unserem Modell wird i₀ an gemessene Überspannungen kalibriert (Paper Fig. 3c/3d).

### Was rauskommt
Konzentrations- und Potentialfelder, Stromdichteverteilung entlang der Anode — und die eigentlich relevante Frage: **Kommt der Zn²⁺-Fluss gleichmäßig an der Anode an, oder gibt es Spitzen?** Spitzen bedeuten ungleichmäßige Abscheidung, also Dendriten.

### Was COMSOL grundsätzlich nicht kann
COMSOL hat **keinen Begriff von Atomen**. In seiner Welt:
- Wasser besteht nicht aus Molekülen, sondern ist ein Medium mit einer Dielektrizitätskonstante
- Zn²⁺ ist kein Ion mit sechs Wassermolekülen, sondern eine Zahl `c` an jedem Punkt
- Eine Oberfläche besteht nicht aus Kohlenstoffatomen mit Sauerstoff daran, sondern ist ein Rand mit einer Randbedingung

Und entscheidend: **COMSOL kann Materialeigenschaften nicht herleiten.** Du gibst D, σ und i₀ vor. Es rechnet klaglos auch mit falschen Werten weiter. *Genau hier ist die alte Simulation angreifbar.*

---

## 5. DFT (Dichtefunktionaltheorie)

### Das Problem

Um zu wissen, wie ein Zn²⁺-Ion mit einer Diamantoberfläche wechselwirkt, braucht man Quantenmechanik. Elektronen sind Quantenobjekte, klassische Physik liefert bei chemischer Bindung schlicht falsche Antworten.

Aber: Die Schrödingergleichung exakt für viele Elektronen zu lösen ist **unmöglich**. Die Vielelektronen-Wellenfunktion hängt von 3 Koordinaten **pro Elektron** ab. Bei 100 Elektronen ist das eine Funktion von 300 Variablen. Der Aufwand wächst exponentiell — hoffnungslos.

### Der Trick

Hohenberg und Kohn haben 1964 bewiesen: Man braucht die Wellenfunktion gar nicht. **Alles über den Grundzustand ist eindeutig durch die Elektronendichte n(r) bestimmt** — eine Funktion von nur 3 Koordinaten, völlig egal wie viele Elektronen beteiligt sind.

Damit wird aus einem unmöglichen Problem ein schwieriges, aber lösbares. Walter Kohn bekam dafür 1998 den Chemie-Nobelpreis, und **D**ichte**f**unktional**t**heorie ist heute das Arbeitspferd der Materialsimulation.

**Ein Haken:** Ein Teil der Theorie — das *Austausch-Korrelations-Funktional*, das beschreibt, wie Elektronen einander ausweichen — ist nicht exakt bekannt und muss genähert werden. Die Wahl dieser Näherung (PBE, HSE06, …) ist eine echte Entscheidung mit echten Konsequenzen. Einer der Punkte, die man an der bestehenden Rechnung prüfen sollte.

### Was man konkret macht

1. **Atommodell bauen.** Für dein System: ein Stapel Kohlenstoffatome in Diamantstruktur, entlang der (111)-Ebene geschnitten, oben Sauerstoffatome angebunden, darüber Vakuum, und ein Zn²⁺-Ion in der Nähe. Typisch 50–300 Atome. Das nennt man ein **Slab-Modell**.
2. **Rechnen lassen.** Der Code bestimmt Elektronendichte und Gesamtenergie dieser Anordnung.
3. **Geometrie relaxieren.** Er berechnet die Kräfte auf jedes Atom, verschiebt sie energetisch bergab, rechnet neu — bis sich die Struktur im Energieminimum einpendelt.
4. **Ergebnisse auslesen.**

### Was rauskommt

**Energien** — und Energiedifferenzen sind die Währung der Chemie. Die Adsorptionsenergie ist schlicht eine Subtraktion:

$$E_{\text{ads}} = E_{\text{Oberfläche+Ion}} - E_{\text{Oberfläche}} - E_{\text{Ion}}$$

Stark negativ heißt: bindet stark. Macht man das für vier Oberflächen, kann man sie sortieren — **genau das hat dein Paper getan** (Dia.-O (111) > Dia. (111) > SiO₂).

**Differenzielle Ladungsdichte** — das, was in Figur 5a gezeigt wird. Man berechnet die Elektronendichte des Gesamtsystems und zieht die Dichten der isolierten Einzelteile ab. Was übrig bleibt, zeigt, **wohin sich Elektronen verschoben haben, als die Teile zusammenkamen**. Rote und blaue Blasen markieren Anreicherung und Verarmung. Das ist buchstäblich ein Bild der entstehenden chemischen Bindung. Wenn das Paper sagt, der "electron cloud overlap" sei bei Dia.-O (111) am größten, liest es diese Bilder ab.

### Grenzen
- **Größe:** ein paar hundert Atome sind Routine, tausend ist ein Projekt. Aufwand skaliert etwa mit N³.
- **Zeit:** Standard-DFT ist statisch und bei 0 K. Keine Dynamik, keine Temperatur, keine Entropie.
- **Skala:** Um einen ganzen Separator mit DFT zu rechnen, bräuchte man ~10²⁰ Atome. Das ist nicht "teuer", sondern um etwa siebzehn Größenordnungen absurd.

---

## 6. Phase-Field (Dendritenwachstum) — kurz

Eine elegante Methode, um eine **bewegliche, formverändernde Grenzfläche** zu simulieren, ohne sie explizit verfolgen zu müssen.

Man führt einen Ordnungsparameter φ ein: φ = 1 im festen Zink, φ = 0 im Elektrolyten, mit einem weichen Übergang dazwischen. Dann schreibt man eine Entwicklungsgleichung für φ, gekoppelt an Konzentration und Potential über Butler-Volmer. Beim Abscheiden entwickelt sich φ — und **Dendriten entstehen von selbst aus der Physik**. Man sagt dem Modell nie, es solle einen Dendriten wachsen lassen; die Instabilität ist real und taucht von alleine auf.

Das ist dieselbe mathematische Maschinerie wie bei der Erstarrungssimulation im Guss — nur elektrochemisch statt thermisch getrieben.

**Vorteil:** liefert echte vorhergesagte Morphologie und ist optisch sehr überzeugend in einer Verteidigung.
**Nachteil:** numerisch anspruchsvoll (feines Netz an der Grenzfläche, kleine Zeitschritte), 3D wird schnell teuer. Und Grenzflächenbreite und -mobilität sind *numerische* Parameter, die bei unsauberer Wahl das physikalische Ergebnis verfälschen.

---

## 7. Mehrskalenmodellierung — wie alles zusammenhängt

```
   DFT (VASP)                              COMSOL
   ══════════                              ══════
   Ångström, ~200 Atome                    Mikrometer, Kontinuum
   0 K, statisch                           zeitabhängig
   Quantenmechanik                         PDEs auf einem Netz
   braucht keine Stoffwerte                braucht Stoffwerte ZWINGEND
   ── berechnet Eigenschaften ─┐      ┌─ verbraucht Eigenschaften ─
                               │      │
                               ▼      ▼
               Adsorptionsenergie ──> Oberflächenbelegung
               Desolvatationsbarriere ─> Austauschstromdichte i₀
               Oberflächenladung ─────> Überführungszahl t₊
```

> **In einem Satz: DFT berechnet das, was COMSOL voraussetzt.**

Das ist die Standardarchitektur der modernen Materialsimulation — und es ist strukturell dasselbe wie Rheometer → Moldex3D. Du würdest nie ein Spritzgussbauteil simulieren, indem du jede Polymerkette verfolgst. Du charakterisierst das Material auf kleiner Skala und benutzt diese Charakterisierung auf großer Skala.

---

## 8. Was das für deine Arbeit bedeutet

**Entschieden (Betreuerin, 14.10.):** nur COMSOL, keine DFT — zu rechenintensiv, und die Übertragung atomistischer Ergebnisse ins Kontinuum ist in der Zeit nicht realistisch. Die Abschnitte 5 und 7 bleiben als Hintergrundwissen (das Paper enthält DFT, und das Kapitel zu Simulationsmethoden erwähnt sie kurz).

Das Paper enthält beides, aber **ohne Verbindung**: Im COMSOL-Modell sind die NDs nur „hollow circles" ohne Materialeigenschaften (SI §1.7, `../Literature/paper-summary.md` F1). Statt sie aus DFT abzuleiten, bekommt die ND-Schicht bei uns eine physikalische Eigenschaft, die an Messwerte kalibriert wird:

| Verknüpfung | Wie |
|---|---|
| Feste negative Ladung der ND-Schicht → t₊ | Donnan-Ausschluss, kalibriert an t₊ = 0,69 |
| Prüfung | σ = 2,94 S/m ohne Nachjustieren |
| t₊ → Dendritenbeginn | Sand'sche Zeit, eine Zeile |

Stand und vorgeschlagenes Vorgehen: `../notes/progress.md`.

---

## 9. Werkzeuge

- **COMSOL 6.3** — Hauptwerkzeug, läuft auf dem Laptop. GUI-Workflow wie bei Moldex3D. Nachteil: schlecht versionierbar.
- **Python** — für Auswertung, Parameterrechnungen und Abbildungen. Alternativen zu COMSOL nur als Rückfall: FEniCSx, FiPy (gut für Phase-Field), PyBaMM.

---

## 10. Glossar

| Deutsch | Englisch | Bedeutung |
|---|---|---|
| Finite-Elemente-Methode | FEM | Numerik-Familie, wie Moldex3D |
| Netz, Gitter | mesh | Diskretisierung des Gebiets |
| Randbedingung | boundary condition | Vorgabe am Gebietsrand |
| Stoffwert, Materialparameter | material property | Was das Kontinuummodell braucht |
| Überspannung | overpotential | Spannung über dem Gleichgewicht |
| Austauschstromdichte | exchange current density (i₀) | "Wie leicht läuft die Reaktion" |
| Elektroneutralität | electroneutrality | Vereinfachung: Ladung ≈ 0 überall |
| Slab-Modell | slab model | Atomlagen + Vakuum zur Oberflächendarstellung |
| Funktional | functional | Die zentrale DFT-Näherung (PBE, HSE06) |
| Pseudopotential | pseudopotential | Ersetzt chemisch inaktive Rumpfelektronen |
| Abschneideenergie | plane-wave cutoff | Basissatzgröße — DFT-Analogon zur Netzverfeinerung |
| k-Punkte | k-points | Abtastung des reziproken Raums |
| Relaxation | relaxation | Atome ins Energieminimum verschieben |
| Adsorptionsenergie | adsorption energy | Energiegewinn beim Anbinden |
| NEB | nudged elastic band | Findet echte Reaktionsbarrieren |
| Mehrskalenmodellierung | multiscale modelling | Kopplung über Längenskalen |
