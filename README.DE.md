# Kodi4Seniors

English: [README.md](README.md)

Kodi4Seniors ist ein Kodi-Skin-Paket für einen Seniorenhaushalt. Kodi bleibt für Betreuung und Wartung vollwertig nutzbar, während die tägliche Oberfläche ruhig und einfach bleibt: Fernsehen, Mediatheken und vorbereitete Bibliothek.

## Zielnutzung

- Primäre Zielgruppe: Seniorenhaushalt
- Primäre Sprache: Deutsch, Englisch wird parallel gepflegt
- Zielgerät: Fire TV mit Kodi
- Bedienung: normale TV-Fernbedienung über HDMI-CEC oder Fire-TV-Fernbedienung
- Alltag: Pfeiltasten, OK, Zurück, Home/Power

## Hauptbereiche im Alltag

| Bereich             | Zweck                                           |
| ------------------- | ----------------------------------------------- |
| Live TV             | Fernsehen, Senderliste und EPG                  |
| Mediatheken         | ARD und ZDF als bevorzugte Einstiegspunkte      |
| Bibliothek          | Vorbereitete lokale Videoinhalte                |
| Betreuung / Technik | Geschützter Bereich für Einrichtung und Wartung |

Die Betreuer-PIN ist ein Versehschutz, keine echte Sicherheitsgrenze.

## Repository-Struktur

- `skin.kodi4seniors/`: installierbarer Kodi-Skin
- `skin.kodi4seniors/1080i/`: Skin-Fenster und Include-Definitionen
- `scripts/build_release.py`: baut das Release-ZIP
- `scripts/publish_to_repo.py`: publiziert den Skin nach `mildman1848.github.io`
- `scripts/validate_repo.py`: prüft XML, Versionen, Pflicht-Assets und Release-ZIP-Inhalt
- `docs/`: Produkt-, Setup-, Fernbedienungs-, Recovery- und Roadmap-Dokumentation

## Dokumentation

- [Produktvision](docs/product-vision.md)
- [Setup-Playbook](docs/setup-playbook.md)
- [Fernbedienung und Navigation](docs/remote-control.md)
- [Recovery und Wartung](docs/recovery.md)
- [Roadmap](docs/roadmap.md)
- [Implementierungsplan](docs/implementation-plan.md)

## Lokale Validierung

```bash
npm ci
npm run validate
```

Die Validierung prüft:

- Python-Hilfsskripte
- alle Skin-XML-Dateien
- Versionsgleichheit zwischen `addon.xml`, `package.json` und `VERSION`
- notwendige Skin-Assets
- Inhalt des Release-ZIPs

## Release bauen

```bash
npm run build
```

Das ZIP wird nach `dist/` geschrieben und kann als Kodi-Skin-Add-on installiert werden.
