# TESTING.md

## Grundsatz

Eine Aufgabe ist nicht abgeschlossen, nur weil sie im Editor funktioniert. Jede Aenderung braucht automatisierte Tests oder eine klar dokumentierte manuelle Validierung.

## Teststufen

### 1. Domain- und Unit-Tests

Ohne komplette 3D-Szene pruefen:

- Avatar-Datenmodell und Defaults
- Savegame-Serialisierung
- Schema-Migrationen
- Inventar- und Wirtschaftsregeln
- Pflanzenzustandswechsel
- Interaktionsauswahl und Reichweite
- Fahrzeugzustandswechsel

### 2. Szenen- und Integrationstests

Mit kleinen isolierten Testszenen pruefen:

- Spielfigurbewegung und Kollision
- Kamera und Hindernisschutz
- Animationstransitionen
- Werkzeugaufnahme und -nutzung
- Fahrzeug betreten und verlassen
- Character-Customizer
- Save/Load in verschiedenen Laufzeitzustaenden

### 3. Android-Geraetetests

Mindestens pruefen:

- Installation und Start
- Touch-Steuerung
- UI-Skalierung
- Berechtigungen und Dateispeicherung
- Frametimes, Speicher und Ladezeiten
- App-Wechsel, Pause und Wiederaufnahme
- thermische Stabilitaet bei laengerer Sitzung

### 4. Smoke-Test fuer jeden Pull Request

- Projektstruktur ist vollstaendig.
- Keine Secrets oder verbotenen Binaerdateien.
- Dokumentverweise sind gueltig.
- Relevante Unit-Tests laufen.
- Export-/Build-Konfiguration ist syntaktisch gueltig.

## Avatar-MVP-Testmatrix

| Bereich | Test | Erwartung |
|---|---|---|
| Datenmodell | fehlende optionale Felder | sichere Defaults |
| Datenmodell | unbekannte Asset-ID | definiertes Fallback |
| Migration | alte Schema-Version laden | Daten werden verlustarm migriert |
| Customizer | alle Preset-Kombinationen | keine ungueltigen Referenzen |
| Bewegung | Ebene, Rampe, Kante | stabil und ohne Durchfallen |
| Kamera | Wand hinter Figur | Kamera bleibt vor Hindernis |
| Interaktion | mehrere Ziele | deterministische Prioritaet |
| Fahrzeug | blockierter Ausstieg | alternativer Punkt oder Abbruch |
| Savegame | Speichern im Fahrzeug | Zustand wird korrekt wiederhergestellt |
| Android | Touch-Steuerung | vollstaendig ohne Tastatur nutzbar |

## Performance-Erfassung

Fuer jedes relevante Profiling festhalten:

- Testgeraet und Betriebssystem
- Build-Typ
- Szene und Anzahl sichtbarer Charaktere
- durchschnittliche und schlechte Frametimes
- Speicherverbrauch
- Draw Calls und Materialien
- Ladezeit
- bekannte thermische Drosselung

Konkrete Zielwerte werden nach dem ersten Android-Prototyp in einem ADR festgelegt.

## Fehlerbericht

Jeder reproduzierbare Fehler soll enthalten:

- Umgebung und Commit
- exakte Schritte
- erwartetes und tatsaechliches Ergebnis
- Log oder Screenshot, sofern vorhanden
- Schweregrad
- Regression ja/nein

## Testabschluss im Agentenboard

Nicht nur `Tests bestanden` schreiben, sondern konkrete Befehle, Szenen oder Geraetetests samt Resultat nennen.