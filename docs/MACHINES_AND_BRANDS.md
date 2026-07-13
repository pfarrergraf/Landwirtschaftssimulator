# Maschinen und Marken

## Startinventar

Exakt vier Fahrzeuge:

1. gebrauchter Fendt-Traktor als geplanter Markeneintrag
2. kleiner Fliegl-Anhaenger als geplanter Markeneintrag
3. grosser Krampe-Anhaenger als geplanter Markeneintrag
4. gebrauchter CLAAS-Maehdrescher als geplanter Markeneintrag

John Deere wird im erweiterten Katalog fuer Traktoren, Mähdrescher und Feldhaecksler vorgesehen.

## Datenmodell

- `brand` und `model`: Anzeige- und Lizenzmetadaten
- `license_status`: planned, contact_requested, pending, licensed, rejected, fictional_replacement
- `asset_status`: primitive_placeholder, neutral_model, licensed_model
- `game_price_eur`: Balancingwert
- `technical_class`: spielrelevante Leistungsklasse

## Grundsatz

Markennamen im internen Plan sind keine Erlaubnis fuer Logos, Modellformen, Produktfotos oder werbliche Partnerschaftsbehauptungen. Jeder Release kann per Konfiguration auf neutrale Ersatzmarken umgestellt werden.
