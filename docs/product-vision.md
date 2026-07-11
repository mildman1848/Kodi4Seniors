# Produktvision: Kodi4Seniors

## Ziel

Kodi4Seniors soll ein vollwertiger Kodi-Skin für einen Seniorenhaushalt sein: im Alltag sehr einfach, in der Betreuungsebene vollständig genug für Einrichtung, Wartung und Fehlerbehebung.

## Primäre Zielgruppe

- Seniorinnen und Senioren in einem privaten Haushalt
- Bedienung über normale TV-Fernbedienung mit HDMI-CEC
- Zielplattform zunächst Fire TV mit Kodi
- Technische Einrichtung durch eine betreuende Person

## Produktprinzipien

1. **Alltag zuerst:** Fernsehen, Mediatheken und Bibliothek müssen mit möglichst wenigen Tastendrücken erreichbar sein.
2. **Vollwertig, aber geschützt:** Der Skin darf Kodi nicht kastrieren. Komplexe Einstellungen gehören hinter den Technik-/Betreuungsmodus.
3. **Nur Standardtasten voraussetzen:** Pfeile, OK, Zurück, Home und Power reichen aus.
4. **Deutsch primär:** Alle nutzernahen Texte werden primär deutsch gepflegt; Englisch bleibt parallel aktuell.
5. **PIN ist Versehschutz:** Die Betreuer-PIN schützt vor versehentlichen Änderungen, nicht vor einem Angreifer.
6. **Komplettpaket statt losem Skin:** Skin, Setup-Playbook, Recovery-Doku, Release-ZIP und optionales Repository-Publishing gehören zusammen.

## Hauptkacheln

Die Startseite bleibt bei vier Hauptbereichen:

| Kachel              | Zweck                                      |          Alltag sichtbar |
| ------------------- | ------------------------------------------ | -----------------------: |
| Live TV             | Fernsehen / EPG / Senderliste              |                       ja |
| Mediatheken         | ARD und ZDF als bevorzugte Einstiegspunkte |                       ja |
| Bibliothek          | vorbereitete lokale Inhalte                |                       ja |
| Betreuung / Technik | Einrichtung, Wartung, Add-ons, System      | versteckt bzw. geschützt |

## Inhaltsfokus

Initial fest eingeplant:

- ARD Mediathek
- ZDF Mediathek
- Live-TV / PVR
- lokale Video-Bibliothek

Nicht für die erste Produktlinie eingeplant:

- Audiobookshelf als eigene Hauptkachel
- Komplettes vorkonfiguriertes Image
- Cloud-Setup-Automation

## Akzeptanzkriterien

- Eine nicht-technische Person findet Live-TV ohne Erklärung.
- Mediatheken sind über eine klare, große Oberfläche erreichbar.
- Technik-/Kodi-Einstellungen sind nicht versehentlich erreichbar.
- Eine betreuende Person kann Installation, Update und Recovery aus der Doku durchführen.
- `npm run validate` prüft alle Skin-XML-Dateien, Versionskonsistenz und Release-Artefakt.
