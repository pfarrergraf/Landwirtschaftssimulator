# Intensiver Repository-Plan

## 1. Ziel

Das Repository soll so organisiert sein, dass ein Coding-Agent in einem Linux-Container den groessten Teil des Projekts planen, implementieren, testen und als Pull Request bereitstellen kann. Die Workstation wird erst fuer visuelle Endkontrolle, aufwendige 3D-Produktion und reale Android-Geraetetests benoetigt.

## 2. Containerfaehige Arbeitsbereiche

Vollstaendig im Container moeglich:

- Produkt- und Game-Design-Dokumentation
- GDScript-Quellcode und Godot-Szenentexte
- Datenkataloge fuer Felder, Kulturen, Maschinen, Wirtschaft und Schwierigkeit
- Python-Validatoren und Balancing-Simulationen
- Savegame-Schemata und Migrationen
- Unit-, Regression- und Headless-Tests
- statische Cloudflare-Webseite
- GitHub Actions und Releasekonfiguration
- Android-Debugbuild in GitHub Actions
- Platzhalterassets aus einfachen primitiven Formen oder rechtssicheren Quellen

Nicht vollstaendig im reinen Container abschliessbar:

- Qualitaetsbeurteilung komplexer 3D-Animationen
- Touchgefuehl und thermische Last auf echten Geraeten
- Store-Signierung ohne bereitgestellte Secrets
- Markenlizenzierung und rechtliche Freigabe
- finale 3D-Fahrzeugmodelle, sofern sie nicht rechtssicher beschafft wurden

## 3. Entwicklungsstrategie

### Phase A: Regeln vor Grafik

Der erste echte Code bildet ein komplettes Wirtschaftsjahr ohne 3D ab. Eingaben sind Anbauplan, Maschinenstrategie und Verkaufszeitpunkt. Ausgabe sind Ertrag, Kosten, Gewinn und Lernfeedback.

### Phase B: Godot als Adapter

Godot liest dieselben Katalogdaten, zeigt den Hof und ruft klar definierte Anwendungsfaelle auf. UI und 3D-Szenen enthalten keine Preis- oder Ertragsformeln.

### Phase C: Vertikaler Schnitt

Drei Felder, zwei Kulturen, vier geerbte Fahrzeuge, Kaufen/Mieten, Ernte und Verkauf. Dieser Schnitt muss auf Android komplett spielbar sein, bevor die Welt vergroessert wird.

### Phase D: Skalierung

Zehn Felder, acht Kulturen, vier Schwierigkeitsstufen, mehr Maschinen, Unterrichtsmaterial und spaeter Tiere.

## 4. Branch- und Pull-Request-Modell

- `main`: immer dokumentiert und testbar.
- `planning/*`: Produkt-, Rechts- oder Architekturplanung.
- `feature/*`: genau ein vertikaler Funktionsschnitt.
- `data/*`: Katalog- und Balancingaenderungen.
- `fix/*`: Fehlerkorrekturen.

Jeder Pull Request enthaelt Ziel, Nicht-Ziele, Testnachweis, Datenmigration, Lizenzstatus und mobile Auswirkungen.

## 5. Meilenstein-Gates

- M0 endet, wenn Containerchecks gruen sind.
- M1 endet, wenn ein Wirtschaftsjahr deterministisch simuliert wird.
- M2 endet, wenn Godot Kataloge und Savegame laedt.
- M3 endet, wenn Fahrzeuge mit Platzhaltern fahrbar sind.
- M4 endet, wenn ein Kind den Kreislauf ohne Entwicklerhilfe abschliessen kann.
- Storearbeit beginnt erst nach Datenschutz-, Lizenz- und Geraetegates.

## 6. Datenhoheit

Alle wirtschaftlichen Werte sind Spiel- und Balancingwerte. Quellen und Aktualisierungsdatum werden getrennt dokumentiert. Reale Marken sind Metadaten; Buildassets bleiben neutral, solange keine Freigabe vorliegt.

## 7. Agentenfaehigkeit

Ein Agent kann anhand von `TASKS.md` den naechsten freien Punkt waehlen. Vor jeder Implementierung prueft er Entscheidungen, Tests und Lizenzstatus. Nach jedem Arbeitspaket aktualisiert er Dokumentation und Testfaelle.
