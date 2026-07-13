# DECISIONS

## ADR-001: Android als Primaerplattform

Status: accepted. Android bietet die beste Kombination aus 3D-Leistung, Offlinebetrieb, Touch und Verteilung. Die Webseite bleibt Begleiter und spaetere Demo.

## ADR-002: Godot 4.7 stable und GDScript

Status: accepted. Mobile Renderer, typisiertes GDScript und exportierbare Android-/Webziele. Versionen werden gepinnt und nur ueber eigenes Upgrade-ADR geaendert.

## ADR-003: Simulation getrennt von 3D

Status: accepted. Balancing und Regeln muessen ohne Renderer testbar sein.

## ADR-004: Offline-Kinderprofile

Status: accepted. Kein Pflichtkonto, keine E-Mail und keine Cloud fuer den ersten Release.

## ADR-005: Reale Marken nur als kontrollierte Datenebene

Status: accepted. Namen wie CLAAS, Fendt und John Deere koennen fuer Planung und Lizenzanfragen erfasst werden. Logos, Markenfarben, Modellformen und kommerzielle Darstellung werden erst nach Freigabe aktiviert.

## ADR-006: Vier geerbte Fahrzeuge

Status: accepted. Jeder neue Hof besitzt exakt einen Traktor, zwei Anhaenger und eine Getreide-Erntemaschine. Anbaugeraete sind separates Hofinventar.

## ADR-007: Vier Schwierigkeitsprofile, ein Simulationskern

Status: accepted. Keine separaten Spiele. Profile steuern Automatisierung, Detailtiefe, Fehlerfolgen und Erklaerungen.

## ADR-008: Container als Referenz fuer Planung und Daten

Status: accepted. Python-Werkzeuge verwenden `uv`; keine Workstation-Pfade. 3D-Performance und reale Android-Geraetetests bleiben spaetere Hardware-Gates.

## ADR-009: Kein Laufzeit-KI-Zwang

Status: accepted. KI darf spaeter bei Entwicklung, Sprache oder Assetprototypen helfen, ist aber kein erforderlicher Bestandteil des Kinderspiels.

## ADR-010: Lizenz vor Veroeffentlichung

Status: accepted. Bis zur schriftlichen Freigabe nutzt der Build neutrale Platzhalterassets, selbst wenn echte Markenbezeichnungen in internen Katalogen erfasst sind.

## ADR-011: Python-Referenzsimulation fuer P1

Status: accepted. Der containerfaehige Python-Kern ist die ausfuehrbare Regelspezifikation fuer Kalender, Felder, Wirtschaft, Maschinen und Savegames. Godot bleibt der Android-Client und muss dieselben Datenvertraege und Invarianten einhalten.

## ADR-012: 360-Tage-Spielkalender

Status: accepted. Ein Spieljahr besitzt zwoelf Monate mit je 30 Tagen. Dadurch bleiben Berechnungen, Unterrichtsaufgaben und Zeitspruenge nachvollziehbar. Saisonzuordnung: Winter Dezember bis Februar, Fruehling Maerz bis Mai, Sommer Juni bis August, Herbst September bis November.
