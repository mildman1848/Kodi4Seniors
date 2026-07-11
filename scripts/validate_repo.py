#!/usr/bin/env python3
"""Repository validation for Kodi4Seniors.

Checks are intentionally stdlib-only so local validation does not depend on
xmllint or extra Python packages.
"""

from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path
from typing import NoReturn
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
ADDON_DIR = ROOT / "skin.kodi4seniors"
ADDON_XML = ADDON_DIR / "addon.xml"
PACKAGE_JSON = ROOT / "package.json"
VERSION_FILE = ROOT / "VERSION"
DIST_DIR = ROOT / "dist"
EXPECTED_ADDON_ID = "skin.kodi4seniors"
REQUIRED_ASSETS = [
    ADDON_DIR / "resources/icon.png",
    ADDON_DIR / "fanart.jpg",
    ADDON_DIR / "resources/screenshot-home.jpg",
]


def fail(message: str) -> NoReturn:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_xml(path: Path) -> ElementTree.Element:
    try:
        return ElementTree.parse(path).getroot()
    except ElementTree.ParseError as err:
        fail(f"XML parse failed for {path.relative_to(ROOT)}: {err}")


def addon_version() -> str:
    root = parse_xml(ADDON_XML)
    addon_id = root.attrib.get("id")
    if addon_id != EXPECTED_ADDON_ID:
        fail(f"addon.xml id is {addon_id!r}, expected {EXPECTED_ADDON_ID!r}")
    version = root.attrib.get("version")
    if not version:
        fail("addon.xml has no version")
    assert version is not None
    return version


def check_all_xml() -> None:
    xml_files = sorted(ADDON_DIR.rglob("*.xml"))
    if not xml_files:
        fail("No XML files found in skin payload")
    for path in xml_files:
        parse_xml(path)
    print(f"xml_parse=ok files={len(xml_files)}")


def check_versions() -> str:
    addon = addon_version()
    package = json.loads(PACKAGE_JSON.read_text(encoding="utf-8"))["version"]
    version_file = VERSION_FILE.read_text(encoding="utf-8").strip()
    versions = {"addon.xml": addon, "package.json": package, "VERSION": version_file}
    if len(set(versions.values())) != 1:
        fail("Version mismatch: " + ", ".join(f"{k}={v}" for k, v in versions.items()))
    print(f"version_consistency=ok version={addon}")
    return addon


def check_assets() -> None:
    for path in REQUIRED_ASSETS:
        if not path.exists():
            fail(f"Required asset missing: {path.relative_to(ROOT)}")
        if path.stat().st_size < 1024:
            fail(f"Required asset looks too small: {path.relative_to(ROOT)}")
    print("required_assets=ok")


def check_release_zip(version: str) -> None:
    archive = DIST_DIR / f"{EXPECTED_ADDON_ID}-{version}.zip"
    if not archive.exists():
        fail(f"Release archive missing: {archive.relative_to(ROOT)}")
    with zipfile.ZipFile(archive) as zf:
        names = set(zf.namelist())
        required = {
            f"{EXPECTED_ADDON_ID}/addon.xml",
            f"{EXPECTED_ADDON_ID}/1080i/Home.xml",
            f"{EXPECTED_ADDON_ID}/1080i/Includes.xml",
            f"{EXPECTED_ADDON_ID}/resources/icon.png",
        }
        missing = sorted(required - names)
        if missing:
            fail("Release archive missing required files: " + ", ".join(missing))
        forbidden_prefixes = (".git/", "dist/", "tmp/", "node_modules/")
        forbidden = sorted(name for name in names if name.startswith(forbidden_prefixes))
        if forbidden:
            fail("Release archive contains forbidden paths: " + ", ".join(forbidden[:10]))
    print(f"release_zip=ok file={archive.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-zip", action="store_true", help="also validate the built dist ZIP")
    args = parser.parse_args()

    check_all_xml()
    version = check_versions()
    check_assets()
    if args.release_zip:
        check_release_zip(version)


if __name__ == "__main__":
    main()
