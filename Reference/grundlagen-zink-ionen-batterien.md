# Grundlagen: Zink-Ionen-Batterien

Erklärt für jemanden, der Li-Ionen gut kennt. Englische Fachbegriffe stehen in Klammern — die brauchst du fürs Schreiben.

---

## 1. Das Grundprinzip

Eine wässrige Zink-Ionen-Batterie (*aqueous zinc-ion battery*, AZIB) besteht aus:

- **Anode:** metallisches Zink, meist als Folie
- **Kathode:** ein Material, das Zn²⁺ aufnehmen kann — meist MnO₂
- **Elektrolyt:** ein Zinksalz in **Wasser**, typisch 1–3 M ZnSO₄, oft mit MnSO₄-Zusatz
- **Separator:** trennt die Elektroden elektrisch, lässt aber Ionen durch

**Entladen:** An der Anode löst sich Zink auf, `Zn → Zn²⁺ + 2e⁻`. Die Zn²⁺-Ionen wandern durch den Elektrolyten zur Kathode und werden dort eingelagert.
**Laden:** umgekehrt — Zn²⁺ wird an der Anode wieder als Metall abgeschieden.

### Der wichtigste Unterschied zu Li-Ionen

Bei Li-Ionen sind **beide** Elektroden Interkalationsmaterialien. Li⁺ wird in Graphit bzw. in ein Schichtoxid eingelagert, das Wirtsgitter bleibt erhalten, es entsteht nirgends Metall.

Bei Zink-Ionen ist die Anode **metallisches Zink**. Es wird abgeschieden und wieder aufgelöst (*plating/stripping*).

> **Merksatz:** AZIBs sind nicht das Zink-Analogon zu Li-Ionen-Batterien, sondern zu **Li-Metall**-Batterien.

Damit gelten alle Probleme, die du von Lithium-Metall kennst — Dendriten, ungleichmäßige Abscheidung, elektrisch abgetrenntes Metall — plus eine Reihe wasserspezifischer Probleme, die es bei Li-Ionen gar nicht gab.

---

## 2. Warum überhaupt Zink?

**Nicht** wegen der Energiedichte. Da verliert Zink klar: ~1,2–1,6 V Zellspannung gegenüber ~3,7 V bei Li-Ionen.

Die Argumente sind andere:

| Vorteil | Grund |
|---|---|
| **Kosten** | Zink ist häufig und billig, kein Kobalt, kein Nickel, kein Lithium |
| **Sicherheit** | Wässriger Elektrolyt ist nicht brennbar. Kein thermisches Durchgehen (*thermal runaway*) |
| **Fertigung** | Kein Trockenraum nötig — Zellen können an Luft gebaut werden. Das ist ein enormer Kostenfaktor |
| **Umwelt** | Ungiftig, gut recycelbar |

**Zielmarkt: stationäre Netzspeicher** (*grid storage*). Dort zählen Kosten pro kWh, Sicherheit und Lebensdauer. Gewicht und Bauraum sind zweitrangig — die Batterie steht in einem Container neben einem Windpark und muss nirgendwo hin.

---

## 3. Die Chemie im Detail

### Zn²⁺ ist zweiwertig — und das ändert alles

Zn²⁺ trägt die doppelte Ladung von Li⁺ bei fast identischem Ionenradius (0,74 Å gegenüber 0,76 Å). Die **Ladungsdichte** ist also etwa doppelt so hoch. Daraus folgt fast die gesamte Chemie:

**Hydratationsenthalpie** (wie fest das Ion seine Wasserhülle hält):
- Li⁺ in Wasser: ca. **−520 kJ/mol**
- Zn²⁺ in Wasser: ca. **−2046 kJ/mol**

Zn²⁺ ist in Wasser kein nacktes Ion. Es liegt als oktaedrischer Hexaaqua-Komplex **[Zn(H₂O)₆]²⁺** vor — sechs Wassermoleküle, sehr fest gebunden.

**Folge 1 — Desolvatation ist eine echte kinetische Barriere.**
Bevor ein Zn²⁺ Elektronen aufnehmen und als Metall abgeschieden werden kann, muss es diese Wasserhülle abstreifen (*desolvation*). Das kostet Energie und ist ein geschwindigkeitsbestimmender Schritt an der Anode. **Genau deshalb redet dein Paper von "accelerated desolvation kinetics"** — eine Oberfläche, die beim Abstreifen hilft, senkt die Barriere für die Abscheidung.

**Folge 2 — mitgeschlepptes Wasser macht Ärger.**
Wasser, das zusammen mit dem Ion an der Anodenoberfläche ankommt, kann dort reduziert werden. Siehe HER weiter unten.

**Folge 3 — langsame Diffusion in der Kathode.**
Eine zweifache Ladung wechselwirkt stark mit dem Wirtsgitter. Zn²⁺ bewegt sich deshalb langsam in Kathodenmaterialien, was die Schnellladefähigkeit begrenzt.

### Das Wasserfenster

Wasser ist thermodynamisch nur über einen Spannungsbereich von **1,23 V** stabil. Darüber oder darunter zersetzt es sich in Sauerstoff bzw. Wasserstoff. Das begrenzt die mögliche Zellspannung hart — und ist der Grund, warum die nächste Sektion überhaupt ein Thema ist.

---

## 4. Die vier Probleme der Zinkanode

Das sind die Bösewichte der gesamten AZIB-Literatur. Wichtig: **sie hängen zusammen**, deshalb hilft es oft mehrfach, wenn man eines löst.

### 4.1 Dendriten
Zink scheidet sich ungleichmäßig ab. Eine kleine Erhebung konzentriert das elektrische Feld, dadurch lagert sich dort mehr Zink an, wodurch die Erhebung wächst — eine klassische positive Rückkopplung. Irgendwann durchsticht ein Dendrit den Separator und die Zelle ist kurzgeschlossen.

**Ursachenkette:** ungleichmäßiger Zn²⁺-Fluss an der Anodenoberfläche → ungleichmäßige Keimbildung → Feldüberhöhung → unkontrolliertes Wachstum.

**Das ist der Grund, warum der Separator hier so wichtig ist** — er bestimmt mit, welches Flussprofil überhaupt an der Anode ankommt.

### 4.2 Wasserstoffentwicklung (*hydrogen evolution reaction*, HER)
Wasser kann reduziert werden: `2H₂O + 2e⁻ → H₂ + 2OH⁻`

Zink-Abscheidung liegt bei −0,76 V vs. SHE, also **unterhalb** des Wasserstoffpotentials. Thermodynamisch müsste HER also gewinnen. Dass AZIBs trotzdem funktionieren, liegt allein an der **hohen kinetischen Überspannung** von Wasserstoff auf Zink in neutralen Sulfatelektrolyten. Das ist eine kinetische Gnadenfrist, keine thermodynamische Sicherheit.

**Schaden:** verbraucht Elektrolyt, erzeugt Gasdruck, kostet Ladung (senkt die Coulomb-Effizienz) und — entscheidend — **erhöht den lokalen pH-Wert** durch die entstehenden OH⁻-Ionen.

### 4.3 Korrosion und Passivierung
Der lokale pH-Anstieg führt zur Ausfällung von **basischem Zinksulfat (ZHS)**, Zn₄SO₄(OH)₆·xH₂O — isolierende Plättchen, die sich auf die Anode legen.

**Schaden:** Teile der Oberfläche werden blockiert. Die restliche aktive Fläche muss denselben Strom tragen, also steigt dort die lokale Stromdichte — und die Abscheidung wird noch ungleichmäßiger. Rückkopplung in Richtung Dendriten.

### 4.4 Totes Zink (*dead zinc*)
Beim ungleichmäßigen Auflösen können Zinkbereiche elektrisch vom Stromableiter abgetrennt werden. Das Zink ist physisch noch da, aber elektrochemisch nutzlos. Permanenter Kapazitätsverlust.

### Die Kopplung

```
ungleichmäßiger Fluss ──> ungleichmäßige Abscheidung ──> Dendriten ──> Kurzschluss
        ▲                          │
        │                          ▼
  Oberfläche blockiert <── ZHS-Passivierung <── lokaler pH-Anstieg <── HER
```

Ein Separator, der den Zn²⁺-Fluss vergleichmäßigt, greift diese Schleife **an ihrem Eingang** an. Das ist die für deine Arbeit zentrale Einsicht.

---

## 5. Separatoren: Warum Glasfaser und nicht PP/PE/PP?

### Was bei Li-Ionen verwendet wird

Polyolefin-Membranen: **PP** (Polypropylen), **PE** (Polyethylen), oder als Dreischichtlaminat **PP/PE/PP** — der Klassiker ist Celgard 2325.

- Dicke: ca. **20–25 µm**
- Porosität: ca. **40 %**
- Herstellung: Polymerfolie wird gereckt, dadurch entstehen schlitzförmige Poren

**Warum ausgerechnet drei Schichten?** Das ist eine Sicherheitsfunktion (*thermal shutdown*). PE schmilzt bei ca. 130 °C, PP erst bei ca. 165 °C. Wenn die Zelle überhitzt, schmilzt die mittlere PE-Schicht und verschließt die Poren — der Ionentransport bricht ab und die Zelle schaltet sich selbst ab. Die äußeren PP-Schichten halten dabei noch die mechanische Integrität. Im Prinzip eine eingebaute Sicherung.

### Warum das in wässrigen Zn-Zellen nicht funktioniert

**1. Hydrophobie — das ist der Hauptgrund.**
Polyolefine sind unpolar und wasserabweisend. Ein wässriger Elektrolyt **benetzt sie schlecht bis gar nicht**. Schlechte Benetzung bedeutet: hoher Widerstand, ungleichmäßiger Kontakt zu den Elektroden, unzuverlässige Performance. Die organischen Carbonat-Elektrolyte bei Li-Ionen benetzen PP/PE dagegen problemlos — das Material passt dort einfach zur Flüssigkeit, hier nicht.

**2. Zu wenig Elektrolytreservoir.**
40 % Porosität bei 25 µm Dicke ist sehr wenig Flüssigkeitsvolumen. Zn-Laborzellen brauchen typischerweise deutlich mehr Elektrolyt, unter anderem weil HER kontinuierlich welchen verbraucht.

**3. Mechanisch zu dünn für Zink.**
Zinkabscheidung ist wesentlich rauer und voluminöser als Li-Interkalation, bei der sich makroskopisch fast nichts bewegt. 25 µm sind schnell durchstoßen.

**4. Die Abschaltfunktion ist überflüssig.**
Wässrige Zellen haben kein thermisches Durchgehen. Das Hauptargument für den Dreischichtaufbau entfällt komplett.

### Warum stattdessen Glasfaser

Verwendet wird meist Laborfilterpapier aus Borosilikat-Glasfaser (Whatman GF/A, GF/D).

| Eigenschaft | Warum es hilft |
|---|---|
| **Hydrophil** | Benetzt sofort und vollständig mit wässrigem Elektrolyt |
| **Sehr hohe Porosität** (>90 %) | Großes Elektrolytreservoir |
| **Chemisch inert** | Stabil im Sulfatelektrolyten über den relevanten pH-Bereich |
| **Thermisch stabil** | Unkritisch, aber praktisch |
| **Billig und sofort verfügbar** | Liegt in jedem Labor im Schrank |
| **Dick** (200–700 µm) | Toleriert raue Zinkabscheidung |

### ⭐ Der entscheidende Punkt

**Glasfaser wurde nie als Batterieseparator entwickelt.** Das ist Laborfilterpapier, das aus Bequemlichkeit übernommen wurde, weil es billig ist, sofort benetzt und nicht mit dem Elektrolyten reagiert.

Genau deshalb ist es in allen Punkten schlecht, die dein Paper aufzählt:

- **ungeordnete Makroporen** (*disordered macroporous structure*) → keinerlei Vergleichmäßigung des Ionenflusses
- **mechanisch schwach** → ein loses Fasergewirr, durch das ein Dendrit ohne Weiteres hindurchwächst
- **chemisch inert** → keine Wechselwirkung mit Zn²⁺, also auch keine Regulierung
- **zu dick** → unnötiger Innenwiderstand und Totvolumen

Es ist ein **Platzhalter**, und das ist in dem Feld auch allen klar. Deshalb ist Separator-Engineering bei AZIBs so ein aktives Forschungsthema — und deshalb existiert die Arbeit deiner Gruppe überhaupt.

*Anmerkung:* Es gibt auch Arbeiten mit modifiziertem PP, Cellulose, Nafion und anderen Membranen. Glasfaser ist der Laborstandard, aber nicht die einzige Option — kommerzielle AZIBs werden mit ziemlicher Sicherheit etwas Besseres brauchen.

### Die drei Hebel eines modifizierten Separators

1. **Chemisch** — Oberflächengruppen, die Zn²⁺ adsorbieren und dadurch gleichmäßig verteilen
2. **Elektrostatisch** — geladene Oberfläche, die Anionen abstößt → höhere Überführungszahl t₊
3. **Mechanisch** — harte Phasen, die Dendriten physisch aufhalten

**Dein ND@GF-Paper behauptet alle drei gleichzeitig** — daher die Formulierung "multifunctional reinforcing phase".

---

## 6. Überführungszahl und Sand'sche Zeit

Das ist die quantitative Brücke zwischen "Separator ist ionenselektiv" und "es entstehen keine Dendriten". Für die Simulation zentral.

In einem binären Elektrolyten tragen Kationen und Anionen gemeinsam den Strom: `t₊ + t₋ = 1`.

Anionen können an den Elektroden nicht verbraucht werden. Unter Stromfluss reichern sie sich deshalb auf einer Seite an und verarmen auf der anderen — es entsteht ein **Konzentrationsgradient**. Dieser Gradient führt irgendwann dazu, dass an der Anodenoberfläche nicht mehr genug Zn²⁺ ankommt, und dann beginnt dendritisches Wachstum.

Die **Sand'sche Zeit** (*Sand's time*) gibt an, wann das passiert:

$$\tau_{\text{Sand}} = \pi D \left(\frac{z_c c_0 F}{2 J t_a}\right)^2$$

mit *D* = ambipolarer Diffusionskoeffizient, *c₀* = Konzentration, *J* = Stromdichte, *t_a* = **Anionen**-Überführungszahl.

**So liest man das:** Erhöht man t₊ (also sinkt t_a), wächst die Sand'sche Zeit **quadratisch**. Der Dendritenbeginn wird deutlich verzögert.

**Wie erhöht ein Separator t₊?** Eine negativ geladene Porenoberfläche stößt Sulfat-Anionen ab (Donnan-Ausschluss), lässt Zn²⁺ aber durch. Eine sauerstoffterminierte Diamantoberfläche (C–O⁻, C=O-Gruppen) ist negativ geladen — **genau das ist der behauptete Mechanismus in deinem Paper.**

---

## 7. Wie man AZIB-Performancedaten liest

### Zn//Zn Symmetrische Zelle (Halbzelle)
Zwei Zinkelektroden, es wird bei konstantem Strom hin- und hergeschaltet. Gemessen wird die **Spannungshysterese** über die Zeit. Versagen = plötzlicher Spannungseinbruch (Kurzschluss) oder starker Anstieg (Passivierung).

> *"3738 h bei 2 mA cm⁻²"* heißt: die Zelle hat 3738 Stunden durchgehalten. Das ist die Schlagzeilen-Kennzahl.

**Wichtiger Vorbehalt:** In symmetrischen Zellen wird dicke Zinkfolie verwendet, die Entladetiefe (*depth of discharge*, DOD) liegt oft **unter 1 %**. Beeindruckende Stundenzahlen können also verbergen, dass nur ein winziger Teil des Zinks überhaupt zyklisiert wird. Das ist ein verbreiteter Kritikpunkt am Feld — und ein Punkt, an dem du in der Arbeit kritische Distanz zeigen kannst.

### Zn//Cu Asymmetrische Zelle → Coulomb-Effizienz
Zink wird auf Kupfer abgeschieden und wieder abgelöst. CE = abgelöste/abgeschiedene Ladung.

> *"CE von 99,6 %"* — nach AZIB-Maßstäben gut. Aber: 0,4 % Verlust pro Zyklus summiert sich. Kommerzielle Zellen brauchen >99,9 %.

### Zn//MnO₂ Vollzelle
Die realistische Konfiguration. Zeigt, ob der Separator auch unter echten Bedingungen funktioniert.

### Kumulative Kapazität
`Stromdichte × Gesamtzeit`. Fairer Vergleich zwischen Papern, weil normiert wird, wie hart die Zelle gefahren wurde.

### Kritische Stromdichte (CCD)
Strom schrittweise erhöhen, bis die Zelle kurzschließt. Der Strom, bei dem die Dendriten gewinnen. **Direkte Kennzahl für Dendritenunterdrückung — und ein sehr gutes Validierungsziel für eine Simulation.**

### EIS (Impedanzspektroskopie)
Wie bei Li-Ionen. Der für AZIBs nützliche Trick: **temperaturabhängige EIS**. Man misst den Ladungstransferwiderstand bei mehreren Temperaturen, trägt ihn im Arrhenius-Plot auf und erhält eine **Aktivierungsenergie**. Diese wird in der Literatur als **Desolvatationsbarriere** interpretiert.

**Das ist für dich wichtig:** eine gemessene Zahl, gegen die man eine simulierte Barriere direkt prüfen kann.

---

## 8. Glossar

| Begriff | Bedeutung |
|---|---|
| AZIB | *Aqueous zinc-ion battery* — wässrige Zink-Ionen-Batterie |
| Plating / Stripping | Abscheiden / Auflösen von Metall |
| ZHS | Basisches Zinksulfat, das passivierende Nebenprodukt |
| HER | *Hydrogen evolution reaction* — parasitäre Wasserstoffentwicklung |
| GF | *Glass fiber* — Glasfaser, der Standardseparator |
| CE | *Coulombic efficiency* — Coulomb-Effizienz |
| CCD | *Critical current density* — kritische Stromdichte |
| DOD | *Depth of discharge* — Entladetiefe |
| Desolvatation | Abstreifen der Hydrathülle vor der Abscheidung |
| t₊ | Überführungszahl (*transference number*) des Kations |
| Ionenselektivität | Zn²⁺ bevorzugt durchlassen, Anionen blockieren |
| Flussvergleichmäßigung | *Flux homogenisation* |
| Sand'sche Zeit | Vorhergesagte Zeit bis zum Dendritenbeginn |
| Überspannung | *Overpotential* |
| Tortuosität | *Tortuosity* — Umwegfaktor der Poren |

---

## 9. Wo dein Paper hier einzuordnen ist

Der ND@GF-Separator ist der Versuch, den Separator von einem **passiven Abstandshalter** in einen **aktiven Flussregler** zu verwandeln — mit drei Mechanismen gleichzeitig:

1. O-terminierte (111)-Diamantflächen **adsorbieren Zn²⁺** → verteilen es gleichmäßig → homogener Fluss
2. Negative Oberflächenladung **stößt Sulfat ab** → höheres t₊ → längere Sand'sche Zeit
3. Diamanthärte **blockiert Durchstoßen** → mechanischer Rückfallschutz

Die 3738 h und 99,6 % CE sind die **Folge**. Deine Arbeit soll den **Mechanismus** erklären und verallgemeinern.
