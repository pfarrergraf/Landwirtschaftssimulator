# Grafikplan für den Landwirtschaftssimulator

## Zielbild

Der Simulator soll eine glaubwürdige, realistische 3D-Landwirtschaftswelt für Android darstellen. Realismus bedeutet hier:

- physikalisch plausible Materialien und Beleuchtung,
- korrekte Größenverhältnisse,
- erkennbare landwirtschaftliche Arbeits- und Wachstumszustände,
- glaubwürdige Maschinenbewegungen,
- hohe visuelle Dichte bei kontrollierter Laufzeit- und Speicherlast.

Fotorealistische Rohdaten ohne Optimierung sind ausdrücklich nicht das Ziel. Alle Assets müssen für mobile Hardware skalierbar sein.

## Architekturentscheidung offen, Assetvertrag stabil

Bis zur endgültigen Engineentscheidung gelten engine-neutrale Austauschformate und Regeln:

- 3D-Austauschformat: glTF 2.0 / GLB,
- Quelldateien: Blender-Dateien mit sauberer Szenenstruktur,
- Koordinaten: metrischer Maßstab, 1 Einheit = 1 Meter,
- Materialien: Metallic-Roughness-PBR,
- Texturen: verlustfreie Quellen, Laufzeitkompression erst beim Import,
- Animationen: getrennte, benannte Clips,
- Kollision: separate vereinfachte Collision-Meshes,
- Herkunft, Lizenz und Generierungsweg werden pro Asset dokumentiert.

Engine-spezifische Importeinstellungen werden erst nach `ARC-001` festgelegt.

## Verbindlicher visueller Stil

### Realismusgrad

- realistische Proportionen und Oberflächen,
- leicht vereinfachte Geometrie auf mittlerer Distanz,
- keine Comic-Überzeichnung,
- keine überstarken Farben oder künstlich hohen Kontraste,
- Verschmutzung, Staub, Feuchtigkeit und Abnutzung als kontrollierte Materialvarianten,
- Maschinen zunächst generisch und markenfrei.

### Maßstab und Kamera

- reale Maschinen- und Pflanzenmaße als Ausgangspunkt,
- Referenzfigur und 1-Meter-Messobjekt in jeder Lookdev-Szene,
- Nahansicht für Maschinen und Pflanzen,
- typische Spielansicht aus erhöhter Drittperson- oder Fahrzeugkamera,
- Fernansicht für große Felder und Landschaft.

## Asset-Namensschema

```text
<bereich>_<objekt>_<variante>_<lod>_<version>
```

Beispiele:

```text
crop_wheat_stage04_lod1_v001.glb
machine_tractor_medium_lod0_v001.glb
field_soil_plowed_wet_mat_v001
```

Keine Leerzeichen, Umlaute oder herstellerspezifischen Markennamen in Dateinamen.

## Qualitätsstufen

Jedes darstellungsrelevante Paket unterstützt mindestens drei Profile:

| Profil | Ziel | Typische Maßnahmen |
|---|---|---|
| Low | ältere oder leistungsschwächere Android-Geräte | kleine Texturen, aggressive LODs, reduzierte Schatten und Dichte |
| Medium | Standardprofil | ausgewogene Texturen, Instancing, mittlere Sichtweite |
| High | leistungsfähige Android-Geräte | höhere Dichte, bessere Schatten, zusätzliche Materialdetails |

Konkrete Geräte und Budgets werden in `QA-030` gemessen und nicht geraten.

## 1. Felder und Boden

### Pflichtzustände

Mindestens folgende Boden- und Feldzustände müssen visuell eindeutig unterscheidbar sein:

1. unbearbeiteter Boden,
2. gepflügter Boden,
3. gegrubberter Boden,
4. Saatbett,
5. frisch gesät,
6. feucht oder beregnet,
7. trocken,
8. verdichtet oder befahren,
9. abgeerntet mit Stoppeln,
10. Ernterückstände oder Mulch,
11. Grünland kurz,
12. Grünland hoch,
13. gemähtes Schwad.

### Technischer Aufbau

- kachelbare PBR-Materialsets,
- getrennte Basis-, Detail- und Makrovariation,
- Masken für Fahrspuren, Feuchtigkeit, Bearbeitungsrichtung und Erntereste,
- richtungsabhängige Furchen und Saatreihen,
- Decals oder Mesh-Strips für Reifenspuren,
- Übergänge ohne harte sichtbare Kachelgrenzen,
- Testfläche mit direktem Vergleich aller Zustände.

### Abnahmekriterien

- Zustand ist aus typischer Spielhöhe erkennbar,
- Material wirkt auch auf großen Flächen nicht repetitiv,
- Nass- und Trockenzustand unterscheiden sich plausibel, nicht nur durch Helligkeit,
- Furchen und Reihen passen zur Maschinenfahrtrichtung,
- Low-, Medium- und High-Profil sind vorhanden.

## 2. Pflanzen und Wachstumsstadien

### Startkulturen

Priorisierte erste Kulturen:

- Weizen,
- Gerste,
- Mais,
- Raps,
- Sonnenblume,
- Kartoffel,
- Zuckerrübe,
- Gras.

Weitere Kulturen folgen nach dem vertikalen Ausschnitt.

### Standardisierte Wachstumsstadien

Jede Kultur liefert mindestens:

| Stage | Bedeutung |
|---|---|
| 00 | Saat / unsichtbar |
| 01 | Keimling |
| 02 | frühes Blattstadium |
| 03 | vegetatives Wachstum |
| 04 | geschlossener Bestand |
| 05 | Blüte oder Fruchtansatz |
| 06 | Reifeentwicklung |
| 07 | erntereif |
| 08 | überreif, vertrocknet oder geschädigt |
| 09 | abgeerntete Stoppeln oder Restpflanzen |

Kulturspezifische Abweichungen werden in `data/crops/` dokumentiert, die Stage-IDs bleiben jedoch stabil.

### Technischer Aufbau

- instanzierbare Pflanzencluster statt einzelner hochauflösender Pflanzen,
- mehrere zufällige Varianten pro Stage,
- LOD0 bis LOD2 sowie Fern-Impostor oder vereinfachte Bestandsdarstellung,
- kontrollierte Windanimation,
- Farb- und Größenvariation innerhalb biologisch plausibler Grenzen,
- separate Masken oder Varianten für trocken, nass, krank und erntereif,
- Reihenabstand und Pflanzdichte aus Simulationsdaten steuerbar.

### Abnahmekriterien

- Wachstumsstadien sind ohne UI-Hinweis unterscheidbar,
- Bestände wirken dicht, aber nicht regelmäßig geklont,
- Reihen und Fahrgassen bleiben sichtbar,
- Windbewegung erzeugt keine Gummi- oder Unterwasserwirkung,
- Fernansicht flimmert nicht stark,
- Erntezustand passt zur Simulation.

## 3. Maschinen und Geräte

### Erstes Maschinenpaket

- kompakter Traktor,
- mittlerer Traktor,
- großer Traktor,
- Pflug,
- Grubber,
- Sämaschine,
- Düngerstreuer,
- Pflanzenschutzspritze,
- Mähwerk,
- Schwader,
- Ballenpresse,
- Anhänger,
- Mähdrescher mit Getreideschneidwerk,
- Maisvorsatz.

### Markenregel

Bis zu einer endgültigen Marken- und Lizenzentscheidung werden ausschließlich:

- generische Formen,
- selbst entwickelte Farbvarianten,
- keine Logos,
- keine geschützten Modellbezeichnungen,
- keine nahezu identischen Nachbauten aktueller Markenmodelle

verwendet.

### Technischer Aufbau

- getrennte bewegliche Baugruppen,
- klar benannte Pivotpunkte,
- Radrotation und Lenkung,
- Federungs- oder Achsbewegung, soweit sichtbar,
- Anhängepunkte und Hydraulikbewegung,
- Arbeits- und Transportstellung,
- rotierende oder oszillierende Werkzeuge,
- separate Kollision,
- LOD0 bis LOD3,
- Materialvarianten sauber, staubig, nass und gebraucht.

### Abnahmekriterien

- reale Größenordnung und Bodenfreiheit,
- funktionale Teile bewegen sich korrekt,
- Anhängepunkte stimmen zwischen Traktor und Gerät überein,
- Arbeitsbreite entspricht Simulationsdaten,
- keine sichtbaren Durchdringungen in Standardanimationen,
- mobile LODs erhalten die erkennbare Silhouette.

## 4. Landschaft, Höfe und Infrastruktur

### Module

- Feldwege und Asphaltstraßen,
- Gräben, Hecken und Feldränder,
- Laub- und Nadelbäume,
- Büsche und Wildgras,
- Hofgebäude,
- Hallen, Silos und Lagerflächen,
- Zäune, Tore und Schilder,
- Strommasten und einfache Infrastruktur,
- Wasserflächen und kleine Bäche.

### Regeln

- modulare, kombinierbare Bauteile,
- regionale Glaubwürdigkeit statt beliebiger Asset-Mischung,
- wiederverwendbare Materialbibliothek,
- Fern-LOD und HLOD für Gebäudegruppen,
- Vegetation mit Instancing und Dichteprofilen.

## 5. Wetter, Licht und Jahreszeiten

### Basisszenarien

- klarer Morgen,
- bewölkter Mittag,
- goldene Abendstimmung,
- leichter Regen,
- starker Regen,
- Nebel,
- trockene Sommerperiode,
- herbstliche Erntezeit.

### Visuelle Zustände

- Bodenfeuchte,
- nasse Maschinenoberflächen,
- Pfützen nur an plausiblen Stellen,
- Staub bei Trockenheit,
- wechselnde Vegetationsfarbe,
- Schattenqualität pro Leistungsprofil,
- reproduzierbare Lookdev-Presets für Vergleiche.

## 6. Asset-Pipeline

### Produktionskette

```text
Referenz -> Blockout -> Maßstabsprüfung -> High/Source Asset -> Retopologie -> UV -> PBR -> LODs -> Collision -> Export -> automatische Validierung -> Engine-Import -> Referenzrender -> Performance-Test
```

### KI-Einsatz

Lokale KI und ComfyUI dürfen eingesetzt werden für:

- Moodboards und Stilreferenzen,
- Texturideen,
- Materialvarianten,
- Schmutz-, Rost- und Abnutzungsmasken,
- Hintergrundelemente und Konzeptansichten.

KI-Ausgaben werden nicht ungeprüft direkt als Laufzeitasset übernommen. Vor Einsatz sind erforderlich:

- Rechte- und Herkunftsdokumentation,
- Artefaktkontrolle,
- nahtlose Kachelung oder saubere UV-Anpassung,
- physikalisch plausible PBR-Kanäle,
- mobile Optimierung.

### Automatische Prüfungen

Die Asset-Pipeline soll prüfen:

- Namensschema,
- Maßeinheit und Bounding Box,
- fehlende Texturen,
- Materialkanäle,
- Polygon- und Vertexbudgets,
- LOD-Vollständigkeit,
- Collision-Mesh,
- Pivot- und Transformregeln,
- verbotene Markenbegriffe,
- Lizenzmetadaten,
- maximale Dateigrößen.

## 7. Visuelle Qualitätssicherung

Jedes Grafikpaket liefert reproduzierbare Referenzbilder:

1. Nahansicht,
2. typische Spielkamera,
3. Fernansicht,
4. Drahtgitteransicht,
5. LOD-Vergleich,
6. neutrale Beleuchtung,
7. mindestens ein Wetterszenario.

Screenshots werden nach festem Kamerapreset erzeugt. Änderungen werden visuell verglichen, nicht nur subjektiv beschrieben.

## 8. Performance-Strategie

### Grundprinzipien

- GPU-Instancing für Pflanzen und wiederholte Objekte,
- LODs und Impostors,
- gebündelte Materialien und Texturatlanten, wo sinnvoll,
- begrenzte transparente Flächen,
- kontrollierte Schattenreichweite,
- Streaming oder sektorweises Laden großer Welten,
- keine unnötigen 4K-Texturen für kleine Objekte,
- Profile für Dichte, Sichtweite und Effekte.

### Messung statt Annahme

Jeder relevante PR dokumentiert:

- Testgerät oder Emulator,
- Auflösung,
- Grafikprofil,
- Szeneninhalt,
- durchschnittliche und ungünstigste Bildrate,
- Speicherverbrauch,
- sichtbare Qualitätsverluste.

## 9. Parallelisierung ohne Konflikte

### Agent A – Felder

- Task: `GFX-010`
- Pfad: `assets/environment/fields/`
- liefert Feldmaterialien und Zustandsvergleich.

### Agent B – Pflanzen

- Task: `GFX-020`
- Pfad: `assets/crops/`
- liefert Kulturen, Stages, Varianten und LODs.

### Agent C – Maschinen

- Task: `GFX-030`
- Pfad: `assets/machines/`
- liefert generische Fahrzeuge, Geräte und Animationen.

### Agent D – Welt

- Task: `GFX-040`
- Pfad: `assets/environment/world/`
- liefert Landschafts- und Hofmodule.

### Agent E – Wetter und Lookdev

- Task: `GFX-050`
- Pfade: `assets/environment/weather/`, `docs/art/lighting/`
- liefert Presets und Materialreaktionen.

### Agent F – Asset-Tools

- Task: `TOOL-001`
- Pfad: `tools/asset_pipeline/`
- liefert Validierung und Konvertierung.

### Agent G – QA

- Tasks: `QA-010`, später `QA-020` und `QA-030`
- Pfade: `tests/assets/`, `tests/visual/`, `tests/performance/`, `docs/qa/`
- liefert automatisierte und visuelle Nachweise.

Keiner dieser Agenten verändert zentrale Registries oder Engine-Projekte. Das übernimmt anschließend ein Integration Agent unter `INT-010`.

## 10. Meilensteine

### M1 – Visual Contract

- Visual Bible,
- Assetvertrag,
- Engineentscheidung vorbereitet,
- ein Testobjekt durch die gesamte Pipeline.

### M2 – Spielbares Testfeld

- ein Feld mit mehreren Bodenständen,
- Weizen in allen Wachstumsstadien,
- ein generischer Traktor mit Sämaschine,
- Tageslicht und Regen,
- Android-Profil Medium.

### M3 – Vertikaler Ausschnitt

- mehrere Kulturen,
- vollständiger Feldzyklus,
- kleine Hofumgebung,
- mehrere Maschinen,
- visuelle Tests und Performance-Matrix.

### M4 – Inhaltsproduktion

- skalierte Assetproduktion,
- weitere Kulturen und Geräte,
- regionale Kartenbausteine,
- saisonale Varianten,
- kontinuierliche Optimierung.

## Definition of Done für Grafikassets

Ein Asset ist erst fertig, wenn:

- Maßstab und Ausrichtung korrekt sind,
- PBR-Materialien vollständig sind,
- erforderliche LODs vorhanden sind,
- Collision und Pivotregeln eingehalten werden,
- Benennung dem Vertrag entspricht,
- Lizenz und Herkunft dokumentiert sind,
- Referenzbilder vorliegen,
- automatische Prüfungen bestehen,
- Android-Performance mindestens im vorgesehenen Profil gemessen wurde,
- Statusdatei und PR-Übergabe vollständig sind.
