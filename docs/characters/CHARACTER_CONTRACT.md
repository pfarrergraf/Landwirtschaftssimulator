# CHR-001 – Charakter- und Avatarvertrag

## Ziel

Die Spielfigur wird als engine-neutrales Domänenobjekt beschrieben. Darstellung, Eingabe, Bewegung, Animation, Interaktion und Persistenz bleiben getrennte Verantwortlichkeiten.

## Kernobjekte

### CharacterIdentity

Unveränderliche oder selten veränderte Identität:

- `character_id`: stabile UUID oder projektweit eindeutige ID,
- `profile_id`: zugehöriges Spielerprofil,
- `display_name`: frei wählbarer Anzeigename,
- `created_at`: ISO-8601-Zeitpunkt,
- `schema_version`: Versionsnummer des Charakterdatensatzes.

### CharacterAppearanceData

Nur stabile Preset-IDs, keine direkten Datei- oder Szenenpfade:

- `body_preset_id`,
- `skin_tone_id`,
- `hair_preset_id`,
- `hair_color_id`,
- `face_preset_id`,
- `top_id`,
- `bottom_id`,
- `footwear_id`,
- `headwear_id`, optional,
- `accessory_ids`, Liste stabiler IDs.

### CharacterRuntimeState

Speicherbarer Laufzeitzustand:

- Welt- oder Karten-ID,
- Position in Metern,
- Rotation als Quaternion oder normierter Yaw-Wert,
- aktueller Bewegungsmodus,
- aktueller Interaktionszustand,
- ausgerüstetes Werkzeug,
- Fahrzeug- und Sitzzuordnung,
- letzter sicherer Bodenpunkt,
- optionale Statuswerte wie Energie nur über versionierte Erweiterungen.

## Bewegungsabsicht

Eingabegeräte erzeugen ausschließlich `MovementIntent`:

- zweidimensionaler Bewegungsvektor,
- Blick- oder Kamerarichtung,
- gewünschte Geschwindigkeit: walk/run,
- springen bleibt im MVP deaktiviert,
- Aktions-, Abbruch- und Werkzeugabsicht.

Tastatur, Gamepad und Touch dürfen unterschiedliche Adapter besitzen, aber keinen unterschiedlichen Domänenvertrag.

## Interaktionsvertrag

Ein interaktives Objekt stellt bereit:

- stabile `interaction_id`,
- Aktionstyp,
- maximale Reichweite,
- Priorität,
- optionale Blickrichtungsanforderung,
- Vorbedingungen,
- lokalisierbaren Anzeigetextschlüssel,
- Ausführungsresultat.

Der Avatar wählt genau einen Fokus nach deterministischen Regeln:

1. nur erfüllte Vorbedingungen,
2. höchste Priorität,
3. kleinste Entfernung,
4. stabiler ID-Vergleich als Tie-Breaker.

## Fahrzeugvertrag

Ein Fahrzeugsitz besitzt:

- `vehicle_id`,
- `seat_id`,
- Ein- und Ausstiegspunkte,
- erlaubte Rollen,
- Belegungszustand,
- Übergabe der Eingabehoheit,
- sicheren Rückgabepunkt für den Avatar.

Ein Zustandswechsel ist atomar:

`on_foot -> entering -> seated -> exiting -> on_foot`

Fehler oder Abbruch dürfen den Avatar nie ohne gültigen Controllerzustand zurücklassen.

## Animationsvertrag

Domänenzustände referenzieren keine Clipnamen. Der Presentation-Adapter bildet folgende semantische Zustände ab:

- idle,
- walk,
- run,
- interact,
- enter_vehicle,
- seated,
- exit_vehicle.

Die Animation darf die Domänenposition nicht unkontrolliert verändern. Root Motion wird für den MVP nur in klar abgegrenzten Ein-/Ausstiegssequenzen geprüft.

## Persistenzregeln

- Savegames speichern stabile IDs und numerische Zustände.
- Assetpfade, Node-Pfade, Objektadressen und Engine-Handles sind verboten.
- Unbekannte optionale Felder dürfen beim Lesen ignoriert werden.
- Fehlende optionale Felder erhalten dokumentierte Standardwerte.
- Jede inkompatible Änderung erhöht die Schema-Hauptversion und benötigt eine Migration.

## MVP-Abnahme

Der Vertrag ist erfüllt, wenn:

1. ein Charakterprofil ohne Engine geladen und validiert werden kann,
2. mindestens zwei Erscheinungspresets austauschbar sind,
3. Tastatur- und Touch-Eingabe denselben `MovementIntent` erzeugen,
4. Interaktionsfokus deterministisch getestet ist,
5. Fahrzeugzustände inklusive Abbruch getestet sind,
6. Speichern und Laden keine direkten Asset- oder Engine-Referenzen benötigt.