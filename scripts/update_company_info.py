#!/usr/bin/env python3
"""Bulk-update company name and address across devicefindhub.com."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_COMPANY = "WHATECH MOBILE CO., LIMITED"
NEW_COMPANY = "WHATECH MOBILE CO., LIMITED"
PERSON = "Huanbin Lin"

NEW_FULL = "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong"
NEW_LINE1 = "Room 505, 5th floor, Beverley Commercial Centre"
NEW_LINE2 = "87-105 Chatham Road South"
NEW_LINE3 = "Hong Kong"

EXTENSIONS = {".html", ".json", ".py", ".md", ".xml", ".txt"}

FOOTER_BLOCK_RE = re.compile(
    r"<li><strong>The Lead Empire L\.L\.C-FZ</strong></li>\s*"
    r"(?:<li>Huanbin Lin</li>\s*)?"
    r"<li>Meydan Grandstand, 6th floor(?:</li>\s*<li>Meydan Road)?(?:, Meydan Road)?(?:, Dubai(?:, (?:United Arab Emirates|Emirati Arabi Uniti|United Arab Emiratesłochy))?)?(?:</li>\s*<li>Dubai(?:, (?:United Arab Emirates|Emirati Arabi Uniti))?)?</li>",
    re.M,
)

BR_BLOCK_RE = re.compile(
    r"<strong>The Lead Empire L\.L\.C-FZ</strong><br>\s*"
    r"Meydan Grandstand, 6th floor<br>\s*"
    r"Meydan Road<br>\s*"
    r"(?:Dubai<br>\s*)?"
    r"(?:United Arab Emirates|Emirati Arabi Uniti)<br>",
    re.M,
)

CONTACT_P_RE = re.compile(
    r"<p>Meydan Grandstand, 6th floor(?:<br>|, )Meydan Road(?:<br>|, )(?:Dubai(?:<br>|, )?)?(?:United Arab Emirates|Emirati Arabi Uniti)(?:łochy)?</p>",
)

JSON_INFO_RE = re.compile(
    r'"<strong>The Lead Empire L\.L\.C-FZ</strong>",\s*'
    r'"Meydan Grandstand, 6th floor",\s*'
    r'"Meydan Road",\s*'
    r'"Hong Kong"\s*\]',
)


def transform(content: str) -> str:
    content = FOOTER_BLOCK_RE.sub(
        "<li><strong>WHATECH MOBILE CO., LIMITED</strong></li>\n"
        "          <li>Huanbin Lin</li>\n"
        "          <li>Room 505, 5th floor, Beverley Commercial Centre</li>\n"
        "          <li>87-105 Chatham Road South</li>\n"
        "          <li>Hong Kong</li>",
        content,
    )

    content = BR_BLOCK_RE.sub(
        "<strong>WHATECH MOBILE CO., LIMITED</strong><br>\n"
        "      Huanbin Lin<br>\n"
        "      Room 505, 5th floor, Beverley Commercial Centre<br>\n"
        "      87-105 Chatham Road South<br>\n"
        "      Hong Kong<br>",
        content,
    )

    content = CONTACT_P_RE.sub(
        "<p>Huanbin Lin<br>"
        "Room 505, 5th floor, Beverley Commercial Centre<br>"
        "87-105 Chatham Road South<br>"
        "Hong Kong</p>",
        content,
    )

    content = JSON_INFO_RE.sub(
        '"<strong>WHATECH MOBILE CO., LIMITED</strong>",\n'
        '      "Huanbin Lin",\n'
        '      "Room 505, 5th floor, Beverley Commercial Centre",\n'
        '      "87-105 Chatham Road South",\n'
        '      "Hong Kong"    ]',
        content,
    )

    # Compact one-line addresses (footers, policies, JSON)
    for old in (
        "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong",
        "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong",
        "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong",
        "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong",
        "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong",
    ):
        content = content.replace(old, NEW_FULL)

    content = content.replace(
        "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong",
        NEW_FULL,
    )

    # Remaining split list items (if regex missed indentation variants)
    content = content.replace(
        "<li>Meydan Grandstand, 6th floor</li>\n          <li>Meydan Road</li>\n          <li>Hong Kong</li>",
        f"<li>{PERSON}</li>\n          <li>{NEW_LINE1}</li>\n          <li>{NEW_LINE2}</li>\n          <li>{NEW_LINE3}</li>",
    )
    content = content.replace(
        "<li>Meydan Grandstand, 6th floor</li>\n          <li>Meydan Road</li>\n          <li>Hong Kong</li>",
        f"<li>{PERSON}</li>\n          <li>{NEW_LINE1}</li>\n          <li>{NEW_LINE2}</li>\n          <li>{NEW_LINE3}</li>",
    )
    content = content.replace(
        "<li>Meydan Grandstand, 6th floor</li>\n        <li>Meydan Road</li>\n        <li>Hong Kong</li>",
        f"<li>{PERSON}</li>\n        <li>{NEW_LINE1}</li>\n        <li>{NEW_LINE2}</li>\n        <li>{NEW_LINE3}</li>",
    )
    content = content.replace(
        "<li>Meydan Grandstand, 6th floor</li>\n        <li>Meydan Road</li>\n        <li>Hong Kong</li>",
        f"<li>{PERSON}</li>\n        <li>{NEW_LINE1}</li>\n        <li>{NEW_LINE2}</li>\n        <li>{NEW_LINE3}</li>",
    )
    content = content.replace(
        "<li>Meydan Grandstand, 6th floor</li>\n          <li>Meydan Road, Dubai</li>\n          <li>Emirati Arabi Uniti</li>",
        f"<li>{PERSON}</li>\n          <li>{NEW_LINE1}</li>\n          <li>{NEW_LINE2}</li>\n          <li>{NEW_LINE3}</li>",
    )

    # Contact card inline <br> without wrapping regex match
    content = content.replace(
        "Huanbin Lin<br>Room 505, 5th floor, Beverley Commercial Centre<br>87-105 Chatham Road South<br>Hong Kong",
        f"{PERSON}<br>{NEW_LINE1}<br>{NEW_LINE2}<br>{NEW_LINE3}",
    )
    content = content.replace(
        "Huanbin Lin<br>Room 505, 5th floor, Beverley Commercial Centre<br>87-105 Chatham Road South<br>Hong Kong",
        f"{PERSON}<br>{NEW_LINE1}<br>{NEW_LINE2}<br>{NEW_LINE3}",
    )

    # Schema.org
    content = content.replace(
        '"streetAddress": "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South"',
        f'"streetAddress": "{NEW_LINE1}, {NEW_LINE2}"',
    )
    content = content.replace('"addressLocality": "Hong Kong"', f'"addressLocality": "{NEW_LINE3}"')
    content = content.replace('"addressCountry": "HK"', '"addressCountry": "HK"')

    # JSON company_address field leftover fragments
    content = content.replace(
        '"company_address": "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong"',
        f'"company_address": "{NEW_FULL}"',
    )

    # Location prose (keep company name replacement last so these still match)
    location_phrases = [
        ("based in Hong Kong", "based in Hong Kong"),
        ("based in Hong Kong", "based in Hong Kong"),
        ("headquarters in Hong Kong", "headquarters in Hong Kong"),
        ("is based in Hong Kong", "is based in Hong Kong"),
        ("con sede a Hong Kong", "con sede a Hong Kong"),
        ("sede a Hong Kong", "sede a Hong Kong"),
        ("sede a Hong Kong", "sede a Hong Kong"),
        ("sede a Hong Kong", "sede a Hong Kong"),
        ("ha sede a Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong", f"ha sede a {NEW_FULL}"),
        ("has their Sitz in Hong Kong", "has their Sitz in Hong Kong"),
        ("mit Sitz in Hong Kong", "mit Sitz in Hong Kong"),
        ("con sede en Hong Kong", "con sede en Hong Kong"),
        ("siège à Hong Kong", "siège à Hong Kong"),
        ("sídlo v Hongkongu", "sídlo v Hongkongu"),
        ("sídlem v Hongkongu", "sídlem v Hongkongu"),
        ("sedež v Hongkongu", "sedež v Hongkongu"),
        ("székhelye Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong", f"székhelye {NEW_FULL}"),
        ("έδρα στο Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong", f"έδρα στο {NEW_FULL}"),
        ("е със седалище в Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong", f"е със седалище в {NEW_FULL}"),
        ("è con sede a Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong", f"è con sede a {NEW_FULL}"),
        ("is based in Hong Kong (Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong)", f"is based in Hong Kong ({NEW_FULL})"),
        ("is based in Hong Kong (Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong)", f"is based in Hong Kong ({NEW_FULL})"),
        ("(Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South, Hong Kong)", f"({NEW_FULL})"),
        ("Hong Kong", "Hong Kong"),
        ("Hong Kong", "Hong Kong"),
        ("Hong Kong", "Hong Kong"),
        ("Hong Kong", "Hong Kong"),
        ("Hong Kong", "Hong Kong"),
        ("Hong Kong", "Hong Kong"),
        ("Hong Kong", "Hong Kong"),
        ("Hong Kong", "Hong Kong"),
        ("Hong Kong", "Hong Kong"),
        ("Hong Kong", "Hong Kong"),
        ("in Hong Kong", "in Hong Kong"),
        ("in Hong Kong", "in Hong Kong"),
        ("a Hong Kong", "a Hong Kong"),
        ("en Hong Kong", "en Hong Kong"),
        ("v Hongkongu", "v Hongkongu"),
        ("w Hongkongu", "w Hongkongu"),
        ("za Hong Kong", "za Hong Kong"),
    ]
    for old, new in location_phrases:
        content = content.replace(old, new)

    content = content.replace(OLD_COMPANY, NEW_COMPANY)

    # Avoid duplicating Huanbin Lin if a leftover address line still sits under the company
    content = content.replace(
        f"<li><strong>{NEW_COMPANY}</strong></li>\n          <li>{NEW_FULL}</li>",
        f"<li><strong>{NEW_COMPANY}</strong></li>\n          <li>{PERSON}</li>\n          <li>{NEW_FULL}</li>",
    )
    content = content.replace(
        f"<li><strong>{NEW_COMPANY}</strong></li>\n        <li>{NEW_FULL}</li>",
        f"<li><strong>{NEW_COMPANY}</strong></li>\n        <li>{PERSON}</li>\n        <li>{NEW_FULL}</li>",
    )
    content = content.replace(
        f"<p><strong>{NEW_COMPANY}</strong></p>\n        <p>{PERSON}<br>",
        f"<p><strong>{NEW_COMPANY}</strong></p>\n        <p>{PERSON}<br>",
    )
    content = content.replace(
        f"<p><strong>{NEW_COMPANY}</strong></p>\n        <p>Huanbin Lin<br>",
        f"<p><strong>{NEW_COMPANY}</strong></p>\n        <p>Huanbin Lin<br>",
    )

    # Deduplicate accidental double person lines
    content = content.replace(
        f"<li>{PERSON}</li>\n          <li>{PERSON}</li>",
        f"<li>{PERSON}</li>",
    )
    content = content.replace(
        f"<li>{PERSON}</li>\n        <li>{PERSON}</li>",
        f"<li>{PERSON}</li>",
    )

    return content


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in EXTENSIONS:
            continue
        if "node_modules" in path.parts or ".git" in path.parts:
            continue
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"updated: {path.relative_to(ROOT)}")
    print(f"\nDone. {changed} files updated.")


if __name__ == "__main__":
    main()
