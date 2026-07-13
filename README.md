# Landwirtschaftssimulator

Planungs- und Entwicklungsrepository fuer eine skalierbare 3D-Landwirtschaftssimulation fuer Android. Das Spiel beginnt als altersgerechte Wirtschafts- und Landwirtschaftssimulation fuer die Klassen 3 und 4 und kann ueber Schwierigkeitsprofile bis zu einer anspruchsvollen Erwachsenensimulation erweitert werden.

## Festgelegte Ausgangslage

- Zielplattform zuerst: Android-App, zusaetzlich statische Cloudflare-Webseite und spaeter reduzierte Web-Demo.
- Engine: Godot 4.7 stable, GDScript, Mobile Renderer.
- Jeder lokale Spieler besitzt einen eigenen Namen, Hofnamen und Spielstand.
- Geerbter Hof: zehn Felder, Hofgebaeude, 100.000 EUR liquide Mittel.
- Geerbte Fahrzeugausstattung: ein Traktor, zwei Anhaenger, eine Erntemaschine.
- Reale Marken duerfen in Planungs- und Datenebene vorkommen, werden aber nur mit geklaerter Lizenz und freigegebenen Assets veroeffentlicht.
- Simulation und 3D-Darstellung bleiben strikt getrennt.
- Planung, Datenmodell, Balancing, Tests, Webseite und CI koennen vollstaendig in Linux-Containern und GitHub Actions entwickelt werden.

## Schnellstart im Container

```bash
uv sync
uv run python -m unittest discover -s tests -v
uv run python tools/validator/validate_data.py
uv run python tools/balancer/simulate_year.py
```

Oder mit Docker:

```bash
docker build -t landwirtschaftssimulator-dev .
docker run --rm landwirtschaftssimulator-dev
```

## Zentrale Dokumente

1. `docs/REPOSITORY_PLAN.md`
2. `docs/PRODUCT_REQUIREMENTS.md`
3. `docs/GAME_DESIGN_DOCUMENT.md`
4. `ARCHITECTURE.md`
5. `ROADMAP.md`
6. `TASKS.md`
7. `docs/LICENSING_AND_BRANDS.md`
8. `docs/CONTAINER_EXECUTION.md`

## Status

Planungsfundament und ausfuehrbare Datenvalidierung. Noch keine produktive 3D-Spielwelt und keine lizenzierten Markenassets.
