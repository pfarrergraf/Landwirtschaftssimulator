# TESTING

## Lokale/containerisierte Pflichtpruefungen

```bash
uv sync
uv run python tools/validator/validate_data.py
uv run python -m unittest discover -s tests -v
uv run python tools/balancer/simulate_year.py
```

## Quality Gates

- Startkapital ist exakt 100.000 EUR.
- Es existieren exakt zehn Startfelder.
- Es existieren exakt vier geerbte Fahrzeuge mit den Kategorien Traktor, zwei Anhaenger und Erntemaschine.
- Alle IDs sind eindeutig.
- Jede reale Marke besitzt `license_status` und `asset_status`.
- Jede Kultur besitzt Kosten, Ertrag, Saison und kompatible Erntekategorie.
- Jede Schwierigkeitsstufe definiert Rundung, Automatisierung und Ausfallfolgen.
- Jahresergebnis ist bei identischem Seed reproduzierbar.

## Spaetere Godot-Gates

- Headless-Projektimport ohne Parserfehler.
- GDScript-Unit-Tests.
- Android-Debugexport.
- Startzeit, Speicherverbrauch, FPS und thermische Stabilitaet auf drei Geraeteklassen.
- Savegame-Migration N-1 auf N.
