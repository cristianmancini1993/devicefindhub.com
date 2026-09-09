#!/usr/bin/env python3
"""Bulk-update company name and address across devicefindhub.com."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_COMPANY = "The Lead Empire L.L.C-FZ"
NEW_COMPANY = "The Lead Empire L.L.C-FZ"

COUNTRY_EN = "United Arab Emirates"
COUNTRY_IT = "Emirati Arabi Uniti"

FULL_ADDR_EN = f"Meydan Grandstand, 6th floor, Meydan Road, Dubai, {COUNTRY_EN}"
FULL_ADDR_IT = f"Meydan Grandstand, 6th floor, Meydan Road, Dubai, {COUNTRY_IT}"

LINE1 = "Meydan Grandstand, 6th floor"
LINE2 = "Meydan Road"
LINE3_EN = f"Dubai, {COUNTRY_EN}"
LINE3_IT = f"Dubai, {COUNTRY_IT}"

OLD_FULL = "Meydan Grandstand, 6th floor, Meydan Road, Dubai, United Arab Emirates"
OLD_LINE1 = "Meydan Grandstand, 6th floor"
OLD_LINE2_COUNTRY = "Dubai, United Arab Emirates"
OLD_LINE2_CITY = "28838 Stresa"
OLD_COUNTRY = "Italy"

STRESA_REPLACEMENTS = [
    ("Dubai (Emirati Arabi Uniti)", "Dubai (Emirati Arabi Uniti)"),
    ("Dubai, VAE", "Dubai, VAE"),
    ("Dubai (JAE)", "Dubai (JAE)"),
    ("Dubai, EAU", "Dubai, EAU"),
    ("Dubai (UAE)", "Dubai (UAE)"),
    ("Dubai (SAE)", "Dubai (SAE)"),
    ("Dubai (JAE)", "Dubai (JAE)"),
    ("Dubai (ZEA)", "Dubai (ZEA)"),
    ("Dubai (Emirati Arabi Uniti)", "Dubai (EAU)"),
    ("sídlo v Dubaji, SAE", "sídlo v Dubaji, SAE"),
    ("sedež v Dubaju, ZAE", "sedež v Dubaju, ZAE"),
    ("sede a Dubai", "sede a Dubai"),
    ("sede en Dubai", "sede en Dubai"),
    ("sídlo v Dubaji", "sídlo v Dubaji"),
    ("sídlem v Dubaji", "sídlem v Dubaji"),
    ("con sede a Dubai", "con sede a Dubai"),
    ("with headquarters in Dubai", "with headquarters in Dubai"),
    ("headquarters in Dubai", "headquarters in Dubai"),
    ("sede a Dubai, EAU", "sede a Dubai, Emirati Arabi Uniti"),
]

EXTENSIONS = {".html", ".json", ".py", ".md", ".xml", ".txt"}


def is_italian(path: Path) -> bool:
    rel = path.as_posix()
    return "/it/" in rel or rel.endswith("/it") or rel.startswith("it/") or "/content/it/" in rel


def country_for(path: Path) -> tuple[str, str]:
    if is_italian(path):
        return COUNTRY_IT, FULL_ADDR_IT
    return COUNTRY_EN, FULL_ADDR_EN


def line3_for(path: Path) -> str:
    return LINE3_IT if is_italian(path) else LINE3_EN


def transform(content: str, path: Path) -> str:
    _, full_addr = country_for(path)
    line3 = line3_for(path)

    content = content.replace(OLD_COMPANY, NEW_COMPANY)

    # Full address variants
    content = content.replace(OLD_FULL, full_addr)
    content = content.replace(
        f"{OLD_LINE1} — {OLD_LINE2_COUNTRY}", full_addr
    )
    content = content.replace(
        f"{OLD_LINE1}, {OLD_LINE2_COUNTRY}", full_addr
    )

    # Multi-line HTML / JSON footer (street + city/country)
    content = content.replace(
        f"{OLD_LINE1}</li>\n          <li>{OLD_LINE2_COUNTRY}</li>",
        f"{LINE1}</li>\n          <li>{LINE2}</li>\n          <li>{line3}</li>",
    )
    content = content.replace(
        f"{OLD_LINE1}</li>\n        <li>{OLD_LINE2_COUNTRY}</li>",
        f"{LINE1}</li>\n        <li>{LINE2}</li>\n        <li>{line3}</li>",
    )
    content = content.replace(
        f'"{OLD_LINE1}",\n      "{OLD_LINE2_COUNTRY}"',
        f'"{LINE1}",\n      "{LINE2}",\n      "{line3}"',
    )
    content = content.replace(
        f'"{OLD_LINE1}",\n      "{OLD_LINE2_COUNTRY}"    ]',
        f'"{LINE1}",\n      "{LINE2}",\n      "{line3}"    ]',
    )

    # about-us / contact-us block with <br>
    content = content.replace(
        f"{OLD_LINE1}<br>\n      {OLD_LINE2_CITY}<br>\n      {OLD_COUNTRY}<br>",
        f"{LINE1}<br>\n      {LINE2}<br>\n      Dubai<br>\n      {line3.split(', ')[1]}<br>",
    )
    content = content.replace(
        f"{OLD_LINE1}<br>\n{OLD_LINE2_CITY}<br>\n{COUNTRY_EN if not is_italian(path) else OLD_COUNTRY}<br>",
        f"{LINE1}<br>\n{LINE2}<br>\nDubai<br>\n{line3.split(', ')[1]}<br>",
    )
    content = content.replace(
        f"<p>{OLD_LINE1}<br>{OLD_LINE2_CITY}<br>{OLD_COUNTRY}</p>",
        f"<p>{LINE1}<br>{LINE2}<br>Dubai<br>{line3.split(', ')[1]}</p>",
    )

    # Remaining partial lines
    content = content.replace(OLD_LINE2_COUNTRY, line3)
    content = content.replace(OLD_LINE1, LINE1)

    # Schema.org in index.html
    content = content.replace(
        '"streetAddress": "Meydan Grandstand, 6th floor"',
        '"streetAddress": "Meydan Grandstand, 6th floor, Meydan Road"',
    )
    content = content.replace('"addressLocality": "Dubai"', '"addressLocality": "Dubai"')
    content = content.replace('"postalCode": ""', '"postalCode": ""')
    content = content.replace('"addressCountry": "AE"', '"addressCountry": "AE"')

    # Stresa contextual mentions
    for old, new in STRESA_REPLACEMENTS:
        content = content.replace(old, new)

    # contact-us meta (Italian)
    content = content.replace(
        "sede a Dubai, EAU, assistenza in italiano",
        "sede a Dubai, Emirati Arabi Uniti, assistenza in italiano",
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
        updated = transform(original, path)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"updated: {path.relative_to(ROOT)}")
    print(f"\nDone. {changed} files updated.")


if __name__ == "__main__":
    main()
