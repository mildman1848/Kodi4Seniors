# Changelog

Deutsch: [CHANGELOG.DE.md](CHANGELOG.DE.md)

All notable changes to this project will be documented in this file.

## 0.1.18 - 2026-03-10

- Replaced the technical bottom focus bar with quieter callout pills and moved the active focus feedback back onto the four tiles.
- Switched the home cards to use the bundled preview artwork more directly so the start screen reads closer to the original mockup.

## 0.1.19 - 2026-03-13

- Reworked the four home tiles so focus, call-to-action text and content blocks match the actually selectable areas more reliably.
- Extended the same clearer focus and guidance model to the Mediatheken hub and technician access screens.

## 0.1.20 - 2026-03-13

- Restored a clearer 2x2 mockup-like color separation on the home screen so the four main areas read as distinct blocks again.
- Replaced german UI fallbacks such as `oe`, `ae` and `ue` with proper umlauts in the updated senior-facing screens.

## 0.1.17 - 2026-03-10

- Made the home focus handler persistent while the start screen is active so focus properties stay in sync as the user moves between tiles.
- Added visible home focus feedback with per-tile "Ausgewaehlt" markers and a bottom status strip showing the active tile and technician lock state.

## 0.1.16 - 2026-03-10

- Expanded `focus_handler.py` into a real home initializer that sets the startup focus to the first tile and publishes the active tile state as window properties.
- Kept directional navigation in XML, but now sync the focused tile label and target for future skin reactions and diagnostics.

## 0.1.15 - 2026-03-10

- Restructured the skin payload around a `1080i/` window folder plus `resources/lib/` and `resources/media/` to match the requested Kodi skin layout more closely.
- Added bundled launcher preview assets, a packaged `focus_handler.py` helper stub and a top-level `fanart.jpg`.
- Updated `addon.xml` metadata to reflect the new folder layout while keeping the addon Kodi-compatible.

## 0.1.14 - 2026-03-10

- Rebuilt the home screen around a simpler fixed four-group layout inspired by the original mockup structure.
- Kept navigation in XML instead of introducing a Python focus handler, because Kodi's native focus model is more robust for this skin.

## 0.1.13 - 2026-03-10

- Tightened the home layout against the mockup with more accurate margins, card heights and row spacing.

## 0.1.12 - 2026-03-10

- Increased the card sizes and redistributed the 2x2 home layout so the screen usage is much closer to the mockup proportions.

## 0.1.11 - 2026-03-10

- Rescaled and repositioned the four home cards to better fill the 1080p screen area and match the mockup proportions.

## 0.1.10 - 2026-03-10

- Removed the automatic `Settings.xml` redirect on load, which was a plausible crash trigger during skin switching.
- Reworked the home screen to visually track the provided mockup more closely: no header on the start screen, four large cards, stronger preview blocks and a calmer settings tile.

## 0.1.9 - 2026-03-10

- Fixed the final outdated `font_MainMenu` font reference so Kodi no longer falls back from `fonts/dejavusans-bold.ttf` for that alias.

## 0.1.8 - 2026-03-10

- Restored the complete shared include foundation from Estuary and moved the senior-specific home/settings includes into a dedicated custom include file.
- Fixed custom window ids for the Mediatheken hub and technician access window.
- Switched font filenames to Estuary-style references so Kodi can resolve the packaged fonts more reliably.

## 0.1.7 - 2026-03-10

- Added a PIN-gated technician mode with a dedicated unlock window before the settings area can be reached.
- Changed the fourth home tile into a caregiver access point while locked and added an explicit action to end technician mode again.

## 0.1.6 - 2026-03-10

- Added a dedicated Mediatheken hub window with grouped entry points for ARD, ZDF, Arte, all video add-ons and the library.
- Improved the TV start tile with dynamic "current" and "next" programme information when Live TV is active.
- Reframed the settings area as a technician-oriented preparation space and added direct setup paths for mediatheken and library preparation.

## 0.1.5 - 2026-03-10

- Aligned the home screen more closely with the original senior-launcher concept: color-coded sections, two larger primary tiles on top and calmer preview-oriented content blocks.
- Improved the semantic distinction between daily-use areas and the technical settings area.

## 0.1.4 - 2026-03-10

- Reworked the home screen into four large tiles in a 2x2 layout instead of a list-style menu.
- Simplified the supporting text on the start screen so the UI reads more like a calm senior launcher and less like a technical skin fork.

## 0.1.3 - 2026-03-10

- Fixed Linux font loading by shipping lowercase font filenames that match the runtime lookups.
- Restored the global include chain in `Includes.xml` so Estuary-derived windows can resolve shared includes and variables.

## 0.1.2 - 2026-03-10

- Bundled the full skin runtime asset set and base XML windows so the skin can actually render screens and dialogs in Kodi.

## 0.1.1 - 2026-03-10

- Fixed missing base windows and dialog files so the skin can be activated more reliably in Kodi.
- Kept the simplified four-tile home screen for Fernsehen, Mediatheken, Bibliothek and Einstellung.

## 0.1.0 - 2026-03-10

- Added the first installable `skin.kodi4seniors` addon skeleton.
- Added a simplified senior-focused home screen with exactly four tiles: Fernsehen, Mediatheken, Bibliothek and Einstellung.
- Added dedicated PVR channel and EPG guide XML views.
- Added local build and publish scripts for the GitHub Pages Kodi repository.
- Added GitHub repository hygiene files, templates and CI workflows.
