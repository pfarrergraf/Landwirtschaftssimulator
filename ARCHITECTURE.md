# ARCHITECTURE

## Architekturziel

Eine deterministische, datengetriebene Landwirtschaftssimulation, deren Kern ohne Grafik in einem Container getestet werden kann. Godot dient als Client und 3D-Darstellung, nicht als alleiniger Speicherort der Geschaeftslogik.

## Schichten

```text
Datenkataloge (JSON)
        |
        v
Simulationsdomain
  - Zeit/Jahreszeiten
  - Felder/Kulturen
  - Maschinen/Arbeit
  - Finanzen/Markt
  - Schwierigkeit/Hilfen
        |
        v
Anwendungsfaelle
  - Neues Profil
  - Anbau planen
  - Arbeit ausfuehren
  - Kaufen/Mieten
  - Ernten/Verkaufen
  - Speichern/Laden
        |
        +--------------------+
        |                    |
        v                    v
Godot Android Client     Python Werkzeuge
3D, UI, Touch, Audio     Validierung, Balancing, Evals
        |
        v
Lokale Spielstaende; optionale Cloud-Dienste spaeter
```

## Monorepo

- `apps/game`: Godot-Projekt fuer Android und spaetere Desktop-/Webexports.
- `apps/website`: statische Cloudflare-Seite.
- `data`: versionierte Spielkataloge und Startzustand.
- `tools`: containerfaehige Validatoren, Balancer und Konverter.
- `tests`: daten- und simulationsbezogene Regressionstests.
- `docs`: Produkt-, Technik-, Rechts- und Releaseplanung.

## Kernprinzipien

1. **Datengetrieben:** Kulturen, Maschinen, Preise und Schwierigkeitsprofile liegen ausserhalb von Szenen.
2. **Deterministisch:** Ein Seed reproduziert Wetter, Markt und Ereignisse.
3. **Progressive Offenlegung:** Dieselbe Simulation, unterschiedliche Sichtbarkeit und Automatisierung je Schwierigkeit.
4. **Offline zuerst:** Kinderprofile und Kernspiel funktionieren ohne Konto und Netzwerk.
5. **Austauschbare Markenebene:** `brand`, `model`, `license_status`, `asset_status` sind getrennt.
6. **Mobile zuerst:** begrenzte Draw Calls, LOD, kleine Texturen, Streaming und kurze Ladewege.
7. **Containerfaehig:** Planung, Daten, Tests, Website und Headless-Checks benoetigen keine lokale Workstation.

## Geplante Godot-Module

```text
apps/game/src/
├── core/          # Zeit, Events, IDs, Seed
├── domain/        # Feld, Kultur, Maschine, Finanzen
├── application/   # Use Cases und Commands
├── persistence/   # Savegame, Migrationen
├── adapters/      # JSON-Kataloge und spaetere Cloudadapter
├── presentation/  # ViewModels, UI-Zustaende
└── world3d/       # Fahrzeuge, Felder, Kamera, Interaktion
```

## Nicht im MVP

Multiplayer, Echtzeit-Backend, Mikrotransaktionen, offene Welt ohne Grenzen, vollstaendige Tierwirtschaft, dynamische Mod-Downloads und generative KI im laufenden Kinderspiel.
