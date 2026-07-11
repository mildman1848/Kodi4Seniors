# Kodi4Seniors Implementation Plan

> **For Hermes:** Use subagent-driven-development skill for later UI-heavy phases. Phase 1 is safe to implement directly because it is docs, validation, and dependency maintenance.

**Goal:** Turn Kodi4Seniors from a thin senior-friendly skin fork into a documented, validated, maintainable senior-household Kodi package.

**Architecture:** Keep the full Kodi/Estuary-derived payload for compatibility, but document and validate the senior-specific product layer. Avoid large XML refactors until validation and recovery documentation are reliable.

**Tech Stack:** Kodi skin XML, Python stdlib validation scripts, npm/prettier, GitHub Actions, GitHub primary plus Codeberg mirror.

---

## Task 1: Stabilize repository validation

**Objective:** Make `npm run validate` portable and broader than the old hand-written `xmllint` file list.

**Files:**

- Create: `scripts/validate_repo.py`
- Modify: `package.json`
- Modify: `.github/workflows/ci.yml`

**Steps:**

1. Parse every `skin.kodi4seniors/**/*.xml` file with Python `xml.etree.ElementTree`.
2. Check version consistency across `skin.kodi4seniors/addon.xml`, `package.json`, and `VERSION`.
3. Build the release ZIP.
4. Check the release ZIP contains required skin files and no forbidden build paths.
5. Run `npm run validate`.

## Task 2: Document product decisions

**Objective:** Capture the answers from the planning session.

**Files:**

- Create: `docs/product-vision.md`
- Create: `docs/roadmap.md`
- Create: `docs/remote-control.md`
- Create: `docs/recovery.md`
- Modify: `docs/setup-playbook.md`
- Modify: `README.md`
- Modify: `README.DE.md`

**Decisions:**

- Target: senior household
- Skin type: full Kodi skin, simple daily layer
- Control: normal TV remote via HDMI-CEC / Fire TV remote
- Main tiles: Live TV, Mediatheken, Bibliothek, protected Betreuung/Technik
- Mediatheken: ARD and ZDF are primary
- Package direction: complete package with docs, release ZIP, recovery path
- Language: German primary, English maintained in parallel
- Settings: hidden/protected from everyday use
- Platform: Fire TV first

## Task 3: Merge safe dependency updates

**Objective:** Bring Dependabot updates current without accepting broken product checks.

**Files:**

- `.github/workflows/*`
- `package.json`
- `package-lock.json`

**Steps:**

1. Merge `actions/checkout` update if substantive CI checks are green.
2. Merge `prettier` update if formatting check is green.
3. Push GitHub and Codeberg.
4. Watch CI.

## Task 4: Prepare later UI work

**Objective:** Leave clear follow-up work for Phase 2.

**Future files:**

- `skin.kodi4seniors/1080i/Includes_Custom.xml`
- `skin.kodi4seniors/1080i/Custom_1112_MediathekenHub.xml`
- `skin.kodi4seniors/1080i/Custom_1113_Technikzugang.xml`
- `skin.kodi4seniors/1080i/DialogButtonMenu.xml`

**Deferred changes:**

- Hide/protect settings more strongly in the everyday UI.
- Make ARD/ZDF fallbacks less technical.
- Replace/update real screenshots.
- Split senior-specific includes into smaller XML files.
