# Container Execution

## Ziel

Jeder Agent oder Entwickler soll ohne Zugriff auf eine bestimmte Workstation arbeiten koennen.

## Referenzbefehle

```bash
uv sync
uv run python tools/validator/validate_data.py
uv run python -m unittest discover -s tests -v
uv run python tools/balancer/simulate_year.py
```

## Docker

```bash
docker build -t landwirtschaftssimulator-dev .
docker run --rm landwirtschaftssimulator-dev
```

## Was der Container nicht vortaeuscht

Ein erfolgreicher Daten- oder Headless-Test beweist keine ausreichende FPS, gute Touchsteuerung oder juristische Markenfreigabe. Diese Punkte besitzen eigene Release-Gates.

## Keine absoluten Pfade

Skripte berechnen das Repository-Root relativ zur eigenen Datei. Keine Pfade wie `/home/benjamin`, `C:\\` oder WSL-Laufwerksmounts verwenden.
