# Kodi4Seniors

Deutsch: [README.DE.md](README.DE.md)

Kodi4Seniors is a senior-household Kodi skin package. It keeps Kodi powerful enough for a caregiver or technician, but presents a calm daily interface for TV, public broadcaster catch-up services, and a prepared video library.

## Target use

- Primary audience: senior household
- Primary language: German, with English documentation maintained alongside it
- Target device: Fire TV running Kodi
- Control: normal TV remote via HDMI-CEC or Fire TV remote
- Daily operation: arrow keys, OK, Back, Home/Power

## Daily home areas

| Area              | Purpose                                     |
| ----------------- | ------------------------------------------- |
| Live TV           | TV, channel list, and EPG                   |
| Mediatheken       | ARD and ZDF as first-class catch-up entries |
| Library           | Prepared local video content                |
| Care / Technician | Protected setup and maintenance area        |

The technician PIN is an accident-prevention guard, not a security boundary.

## Repository structure

- `skin.kodi4seniors/`: installable Kodi skin payload
- `skin.kodi4seniors/1080i/`: skin windows and include definitions
- `scripts/build_release.py`: builds the release ZIP
- `scripts/publish_to_repo.py`: publishes the skin to `mildman1848.github.io`
- `scripts/validate_repo.py`: validates XML, versions, required assets, and release ZIP contents
- `docs/`: product, setup, remote-control, recovery, and roadmap documentation

## Documentation

- [Product vision](docs/product-vision.md)
- [Setup playbook](docs/setup-playbook.md)
- [Remote control and navigation](docs/remote-control.md)
- [Recovery and maintenance](docs/recovery.md)
- [Roadmap](docs/roadmap.md)
- [Implementation plan](docs/implementation-plan.md)

## Local validation

```bash
npm ci
npm run validate
```

Validation checks:

- Python helper syntax
- all skin XML files
- version consistency between `addon.xml`, `package.json`, and `VERSION`
- required skin assets
- release ZIP contents

## Release build

```bash
npm run build
```

The ZIP is written to `dist/` and can be installed as a Kodi skin add-on.
