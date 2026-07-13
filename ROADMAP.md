# ROADMAP.md

## Produktziel

Ein Android-tauglicher 3D-Landwirtschaftssimulator mit glaubwürdiger Feldarbeit, sichtbarem Pflanzenwachstum, generischen Maschinen und einer frei steuerbaren Spielfigur. Die Entwicklung beginnt mit einem kleinen, vollständig spielbaren Loop statt mit einer großen offenen Welt.

## MVP-Spielschleife

1. Spielstand laden oder neu beginnen.
2. Spielfigur erscheint auf einem kleinen Hof.
3. Zum Traktor laufen und interagieren.
4. In den Traktor einsteigen.
5. Sämaschine ankoppeln oder bereits gekoppelt übernehmen.
6. Zum Testfeld fahren.
7. Feld bearbeiten und Weizen säen.
8. Feldzustand und Pflanzenwachstum werden gespeichert.
9. Spiel beenden, neu starten und Zustand korrekt wiederherstellen.

## Meilenstein M0 – Entscheidungsfähige Grundlage

Ergebnis:

- Engineentscheidung mit Android-Spike,
- stabile Feld-, Pflanzen-, Maschinen-, Charakter- und Savegame-Verträge,
- verbindliche Art Bible,
- lokale Repository- und Datenvalidatoren,
- festgelegter MVP-Umfang.

Exit-Kriterien:

- `ARC-001`, `SIM-001`, `CHR-001`, `GFX-001` abgeschlossen,
- kein Kern-Datenmodell hängt direkt von einer Engine-Szene ab,
- ein leerer Android-Testbuild kann reproduzierbar erzeugt werden.

## Meilenstein M1 – Begehbarer Hof

Ergebnis:

- kleine Hof-Testszene,
- mobiler Third-Person-Avatar,
- Kamera, Touch-Steuerung und Desktop-Fallback,
- idle/walk/run Animationen,
- mindestens ein interaktives Hofobjekt,
- erster speicherbarer Charakterzustand.

Exit-Kriterien:

- Avatar läuft auf Android stabil durch die Testszene,
- Kamera durchdringt Standardgeometrie nicht dauerhaft,
- Position und Preset werden gespeichert und geladen,
- Medium-Profil erreicht auf einem definierten Referenzgerät eine stabile Zielbildrate.

## Meilenstein M2 – Fahrbarer Traktor

Ergebnis:

- generischer mittlerer Traktor,
- Spieler kann ein- und aussteigen,
- Input-Besitz wechselt sauber zwischen Avatar und Fahrzeug,
- Basisfahrphysik und Maschinenanimationen,
- Touch-HUD für Fahrzeugsteuerung.

Exit-Kriterien:

- wiederholtes Ein-/Aussteigen ohne festhängende Kamera oder doppelte Eingabe,
- Traktorzustand und Position überstehen Speichern/Laden,
- keine ungeklärten Marken- oder Assetrechte.

## Meilenstein M3 – Spielbares Testfeld

Ergebnis:

- Feld mit klaren Bearbeitungszuständen,
- Sämaschine und einfacher Arbeitsvorgang,
- Weizen als erste Kultur,
- deterministische Feld- und Pflanzenzustände,
- visuelle Synchronisierung zwischen Simulation und Rendering.

Exit-Kriterien:

- der vollständige Aussaat-Loop ist auf Android spielbar,
- Feldzustände bleiben nach Neustart erhalten,
- die Darstellung stimmt mit den Simulations-IDs überein,
- automatisierte Daten- und Savegame-Tests laufen erfolgreich.

## Meilenstein M4 – Erster vertikaler Ausschnitt

Ergebnis:

- kleiner Hof und Testfeld als zusammenhängende Welt,
- Tageszeit und einfaches Wetter,
- Weizenwachstum bis zur Ernte,
- einfache Aufgabenführung,
- Low-, Medium- und High-Grafikprofile,
- reale Gerätetests.

Exit-Kriterien:

- neuer Spieler versteht den ersten Arbeitsauftrag ohne externe Anleitung,
- mindestens ein kompletter Feldzyklus ist möglich,
- keine kritischen Savegame-, Eingabe- oder Speicherfehler,
- dokumentierte Performance-Matrix für mehrere Android-Geräteklassen.

## Meilenstein M5 – Inhaltsproduktion

- weitere Kulturen und Wachstumsvarianten,
- zusätzliche Geräte und Fahrzeugklassen,
- Avatar-Customizer und Kleidungspresets,
- NPC-Grundsystem,
- regionale Landschaftsmodule,
- Wetter- und Saisonvarianten,
- skalierte, automatisiert geprüfte Assetproduktion.

## Meilenstein M6 – Produktreife

- Spielökonomie und Fortschrittssystem,
- Bedienung und Barrierefreiheit,
- robuste Wiederherstellung beschädigter Spielstände,
- Gerätekompatibilität und Langzeittests,
- Datenschutz-, Lizenz- und Store-Vorbereitung,
- Veröffentlichung ausschließlich nach gesonderter Freigabe.

## Nicht im ersten MVP

- Multiplayer,
- große offene Karte,
- vollständige Tierhaltung,
- komplexe NPC-Tagesabläufe,
- lizenzierte Markenmaschinen,
- Cloud-Synchronisierung,
- Echtgeldkäufe oder kostenpflichtige Backenddienste,
- Play-Store-Veröffentlichung.

## Aktueller Fokus

1. `ARC-001` Engineentscheidung mit kleinem Android-Spike.
2. `CHR-001` Charakter-, Avatar- und Interaktionsverträge.
3. `SIM-001` stabile Feld-, Pflanzen- und Maschinen-IDs.
4. `GFX-001` Visual Bible und mobile Assetbudgets.
5. `SAV-001` versionierter Savegame-Vertrag.
6. Danach M1 als erster tatsächlich spielbarer Build.