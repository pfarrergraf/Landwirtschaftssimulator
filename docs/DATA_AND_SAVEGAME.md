# Daten und Savegame

## Kataloge

Kulturen, Maschinen, Felder, Wirtschaft und Schwierigkeit werden als versionierte JSON-Dateien gepflegt.

## Savegame

Geplant ist ein lokales, versioniertes JSON- oder Godot-Resource-Format mit:

- schema_version
- profile_id und frei gewaehlte Anzeigenamen
- Schwierigkeit
- Kalender und Seed
- Konten und Verbindlichkeiten
- Feldzustaende
- Besitz, Mieten und Wartung
- Lager und Vertrage

## Migration

Jede Schemaaenderung benoetigt eine Migration und mindestens einen Test von Version N-1 auf N.
