# AGENTS.md

## Pflichtlekture vor groesseren Aenderungen

Lies zuerst `TASKS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `TESTING.md`, `MODELS.md`, `SECURITY.md`, `SKILLS.md` und `docs/REPOSITORY_PLAN.md`.

## Arbeitsregeln

- Arbeite planungsgetrieben und in kleinen, testbaren Aenderungen.
- Verwende Linux-Container oder GitHub Actions als Referenzumgebung.
- Verwende fuer Python ausschliesslich `uv`, niemals `pip`.
- Bevorzuge Python 3.11 oder 3.12 fuer Werkzeuge; der Spielcode bleibt GDScript.
- Trenne Simulationslogik, Daten, Benutzeroberflaeche und 3D-Assets.
- Keine geheimen Schluessel, Keystores, Markenassets oder proprietaeren Dateien committen.
- Reale Markennamen nur mit `license_status` und austauschbarem Platzhalter verwenden.
- Jede neue Kultur, Maschine oder Schwierigkeit muss durch Datenvalidierung und Tests abgedeckt sein.
- Nach abgeschlossener Arbeit `TASKS.md` und bei Architekturentscheidungen `DECISIONS.md` aktualisieren.
- Kein Scope-Wachstum ohne Aenderung von `ROADMAP.md` und `docs/PRODUCT_REQUIREMENTS.md`.

## Definition of Done

- Daten validieren.
- Tests laufen im Container.
- Dokumentation ist aktualisiert.
- Mobile-Performancebudget wurde beachtet.
- Marken- und Assetstatus ist dokumentiert.
- Keine Workstation-spezifischen absoluten Pfade.
