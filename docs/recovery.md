# Recovery und Wartung

Diese Anleitung ist für die betreuende Person gedacht.

## Wichtige Einordnung

Die Betreuer-PIN ist ein Versehschutz. Sie ist keine echte Sicherheitsgrenze gegen Personen mit Dateizugriff auf Kodi-Profile.

## Skin verlassen

Wenn Kodi4Seniors falsch konfiguriert ist oder die Oberfläche nicht mehr bedienbar wirkt:

1. Öffne den Technik-/Betreuungsbereich.
2. Wechsle in die Kodi-Interface-Einstellungen.
3. Wähle einen Standard-Skin wie Estuary.
4. Starte Kodi neu.

Falls die Oberfläche nicht mehr erreichbar ist, kann die Skin-Einstellung im Kodi-Profil manuell zurückgesetzt werden. Der genaue Profilpfad hängt von der Plattform ab.

## Fire TV typische Pfade

Auf Fire TV liegen Kodi-Daten üblicherweise unter einem Android-App-Datenpfad. Der Zugriff ist je nach Fire-TV-Version eingeschränkt. Praktisch ist meist:

- Kodi-interne Einstellungen zuerst versuchen
- ADB nur für technische Wartung nutzen
- vor Experimenten ein Kodi-Backup erstellen

## PIN zurücksetzen

Wenn die Betreuer-PIN vergessen wurde:

1. Kodi beenden.
2. Kodi-Profil sichern.
3. Skin-Einstellungen im Profil prüfen.
4. `technician_pin` zurücksetzen oder Skin-Einstellungen löschen.
5. Kodi neu starten und PIN neu setzen.

Hinweis: Die genaue Datei kann je nach Kodi-Version variieren. Deshalb vor Änderungen immer das Profil sichern.

## Backup vor Änderungen

Vor größeren Änderungen sichern:

- Kodi-Profilordner
- installierte Add-ons
- PVR-Konfiguration
- Quellen/Bibliothek
- Skin-Einstellungen

## Übergabe-Checkliste

- Standard-PIN geändert oder bewusst dokumentiert
- Recovery-Weg bekannt
- Backup vorhanden
- Fire-TV-Fernbedienung getestet
- TV/CEC-Verhalten getestet
