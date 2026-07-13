# SECURITY.md

## Schutzumfang

Dieses Repository darf keine Geheimnisse, produktiven Zugangsdaten, privaten Schluessel oder nicht freigegebenen personenbezogenen Daten enthalten.

## Secrets

Nicht committen:

- API-Keys und Tokens
- Android-Keystores und Passwoerter
- Store-Zugangsdaten
- private Zertifikate
- Cloud-Service-Credentials
- produktive Datenbankzugriffe

Nur Platzhalter in `.env.example` oder vergleichbaren Beispieldateien verwenden.

## Abhaengigkeiten

- Abhaengigkeiten sparsam einsetzen.
- Herkunft, Version und Lizenz dokumentieren.
- Keine zufaelligen Binaerdateien oder unpruefbaren Downloads in Build-Skripte aufnehmen.
- Neue externe Dienste nur nach Freigabe, wenn Kosten oder Konten entstehen.

## 3D-, Audio- und Grafikassets

Fuer jedes fremde oder generierte Asset dokumentieren:

- Quelle oder Erzeugungsweg
- Autor oder Anbieter
- Lizenz und Nutzungsbedingungen
- Aenderungen
- Datum der Aufnahme
- interne Asset-ID

Nicht erlaubt:

- kopierte proprietaere Assets anderer Landwirtschaftsspiele,
- ungeklärte Rips aus Spielen oder Asset-Paketen,
- Markenlogos und geschuetzte Fahrzeugdesigns ohne geklaerte Nutzung,
- generierte Inhalte ohne nachvollziehbare Rechtebasis.

## Savegames und Nutzerdaten

- lokal nur notwendige Daten speichern,
- Savegames robust gegen Manipulation und Teilkorruption behandeln,
- keine Telemetrie oder Cloud-Synchronisation ohne ausdrueckliche Produktentscheidung,
- Dateipfade und Logs duerfen keine Secrets enthalten.

## Android und Releases

- Debug- und Release-Signierung strikt trennen.
- Keystores niemals im Repository speichern.
- Store-Veroeffentlichungen erfordern ausdrueckliche Freigabe.
- Vor Releases Abhaengigkeiten, Berechtigungen und Datenschutzhinweise pruefen.

## Sicherheitsmeldung

Sicherheitsrelevante Probleme nicht mit echten Secrets in oeffentlichen Issues dokumentieren. Zuerst Geheimnis sperren oder rotieren und nur bereinigte Reproduktionsdaten festhalten.

## Agentenpflicht

Jeder Agent prueft vor Commit mindestens:

- keine Secrets,
- keine unklar lizenzierten Assets,
- keine unbeabsichtigten grossen Binaerdateien,
- keine externen kostenpflichtigen Abhaengigkeiten,
- keine Store- oder Markenentscheidung ohne Freigabe.