# TESTING.md

## Testebenen

### 1. Repository- und Datenvalidierung

- Namensschemata,
- erforderliche Dateien und Metadaten,
- JSON-/YAML-Schemata,
- verbotene Geheimnisse und Markenbegriffe,
- reproduzierbare lokale Befehle.

### 2. Simulationstests

- deterministische Feldzustände,
- Wachstumsübergänge,
- Ertragsberechnung,
- Maschinenparameter und Arbeitsbreiten,
- Randfälle und ungültige Daten.

### 3. Assettests

- Maßstab und Bounding Box,
- Transformationen und Pivotpunkte,
- Materialien und Texturpfade,
- LOD- und Collision-Vollständigkeit,
- Polygon-, Textur- und Dateibudgets,
- Lizenz- und Herkunftsmetadaten.

### 4. Visuelle Tests

Jedes Grafikpaket liefert reproduzierbare Screenshots mit festen Kamera- und Lichtpresets:

- Nahansicht,
- Spielkamera,
- Fernansicht,
- Drahtgitter,
- LOD-Vergleich,
- neutrales Licht,
- mindestens ein Wetterszenario.

### 5. Performance-Tests

Für Android werden Low-, Medium- und High-Profile getrennt gemessen. Jeder Bericht nennt Gerät, Auflösung, Szene, Grafikprofil, Bildrate und Speicherverbrauch.

## Pull-Request-Anforderungen

- Testbefehle müssen im PR aufgeführt sein.
- Nicht ausgeführte Tests benötigen einen konkreten Grund.
- Grafik-PRs benötigen visuelle Nachweise und Assetbudgets.
- Änderungen an Datenverträgen benötigen Migrations- oder Kompatibilitätshinweise.

## Lokale Python-Werkzeuge

Python-Werkzeuge werden ausschließlich mit `uv` ausgeführt, beispielsweise:

```bash
uv sync
uv run pytest
uv run python scripts/validate_repository.py
```

Keine `pip`-Befehle in Dokumentation, CI oder Skripten.
