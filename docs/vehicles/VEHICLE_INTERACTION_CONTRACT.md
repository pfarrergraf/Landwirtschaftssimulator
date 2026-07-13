# Fahrzeug-Interaktionsvertrag

## Ziel

Der erste spielbare Fahrzeugloop erlaubt einer Spielfigur, sich einem generischen Traktor zu nähern, einzusteigen, die Steuerung zu übernehmen, zu fahren und wieder auszusteigen.

## Eingabehoheit

Zu jedem Zeitpunkt besitzt genau ein Objekt die Bewegungs- und Kameraeingabe:

- außerhalb eines Fahrzeugs: `Player`,
- innerhalb eines Fahrzeugs: `GenericTractor`.

Beim Einstieg wird die Spielersteuerung deaktiviert, die Spielerkollision ausgeschaltet, das sichtbare Spielermesh ausgeblendet und die Fahrzeugkamera aktiviert. Beim Ausstieg wird dieser Zustand vollständig zurückgesetzt.

## Interaktionsablauf

1. `InteractionArea` erkennt den Spieler.
2. Der Spieler speichert den Traktor als `interaction_candidate`.
3. Das HUD zeigt die Interaktionsaufforderung.
4. Die Aktion `interact` ruft `request_enter(player)` auf.
5. Der Traktor übernimmt den Spieler als `driver`.
6. Der Spieler wird an `SeatMarker` gebunden.
7. Erneutes `interact` im Fahrzeug ruft `exit_driver()` auf.
8. Der Spieler erscheint an `ExitMarker` und erhält die Kontrolle zurück.

## Sicherheitsregeln

- Ein besetztes Fahrzeug kann nicht erneut betreten werden.
- Ein Spieler ohne erwartete Methoden wird nicht übernommen.
- Beim Ausstieg wird die Referenz auf den Fahrer vor der Rückgabe der Kontrolle gelöscht.
- Der Traktor bleibt vollständig markenfrei und verwendet nur selbst erzeugte Primitive.
- Die Eingabeübergabe darf niemals gleichzeitig Spieler- und Fahrzeugbewegung aktivieren.

## Aktueller Prototypumfang

Enthalten:

- markenfreier Blockout-Traktor,
- einfache Fahrphysik,
- Annäherungsbereich,
- Ein- und Aussteigen,
- getrennte Spieler- und Fahrzeugkamera,
- HUD-Hinweis,
- Tastatursteuerung.

Noch nicht enthalten:

- Radanimation,
- Federung,
- Motor- und Fahrgeräusche,
- Touch-HUD,
- Anhängepunkte,
- Rückwärtsganglogik mit Getriebe,
- Fahrzeugzustand im Savegame,
- reale Android-Geräteprüfung.
