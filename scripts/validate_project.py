#!/usr/bin/env python3
"""Projektvalidering för Romanskaparen-projektet När planen spricker.

Valideringen är avsedd för GitHub Actions och använder bara Python-standardbiblioteket.
Den kontrollerar att projektets kanoniska filer, omslag, publiceringsmetadata och
kapitelserie är konsekventa nog för reproducerbar EPUB/PDF-export.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

CHAPTER_FILE_RE = re.compile(r"^kapitel-(\d{2})\.md$")
CHAPTER_H1_RE = re.compile(r"^#\s+Kapitel\s+(\d+)\s+[–-]\s+(.+?)\s*$")
MARKERS = ("TODO", "FIXME", "[PLACEHOLDER]")

REQUIRED_PATHS = (
    "README.md",
    "roman-bibel.md",
    "synopsis.md",
    "kapitelplan.md",
    "projektstatus.md",
    "project-index.md",
    "kapitel",
    "omslag/nar-planen-spricker-omslag.png",
    "publishing/metadata.yaml",
    "publishing/epub.css",
    "publishing/fix-epub-after-pandoc.py",
    "publishing/pdf-template.tex",
    "publishing/pdf-filter.lua",
    "scripts/build_book.py",
)

REQUIRED_METADATA = {
    "title": "När planen spricker",
    "subtitle": "En roman om förändring, tillit och nya roller",
    "author": "Erland Lindmark",
    "language": "sv-SE",
    "cover-image": "../omslag/nar-planen-spricker-omslag.png",
}


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)


def parse_simple_yaml(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key.strip()] = value
    return values


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        if any(part in {".git"} for part in md.relative_to(root).parts):
            continue
        text = md.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            if " " in target and not target.startswith(("./", "../")):
                target = target.split(" ", 1)[0]
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if not candidate.exists():
                add_error(errors, f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []

    if not root.is_dir():
        add_error(errors, f"Projektkatalogen finns inte: {root}")
        return 1

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            add_error(errors, f"Obligatorisk projektsökväg saknas: {rel}")

    if errors:
        return 1

    metadata = parse_simple_yaml(root / "publishing/metadata.yaml")
    for key, expected in REQUIRED_METADATA.items():
        actual = metadata.get(key)
        if actual != expected:
            add_error(errors, f"Metadata {key!r} är {actual!r}, väntat {expected!r}.")

    cover_rel = metadata.get("cover-image", "").replace("../", "", 1)
    if cover_rel and not (root / cover_rel).is_file():
        add_error(errors, f"Metadata pekar på omslag som saknas: {metadata.get('cover-image')}")

    chapters = sorted((root / "kapitel").glob("kapitel-[0-9][0-9].md"))
    if not chapters:
        add_error(errors, "Inga kapitelfiler hittades.")

    numbers: list[int] = []
    for path in chapters:
        match = CHAPTER_FILE_RE.match(path.name)
        if not match:
            add_error(errors, f"Felaktigt kapitelfilnamn: {path.name}")
            continue
        file_no = int(match.group(1))
        numbers.append(file_no)

        text = path.read_text(encoding="utf-8")
        stripped = text.strip()
        if len(stripped) < 200:
            add_error(errors, f"Kapitlet verkar vara tomt eller för kort: {path.relative_to(root)}")

        first_nonempty = next((line.strip() for line in text.splitlines() if line.strip()), "")
        h1 = CHAPTER_H1_RE.match(first_nonempty)
        if not h1:
            add_error(errors, f"Kapitlet saknar H1 i formatet '# Kapitel N – Titel': {path.relative_to(root)}")
        elif int(h1.group(1)) != file_no:
            add_error(errors, f"Kapitlets H1-nummer matchar inte filnamnet: {path.relative_to(root)}")

        for marker in MARKERS:
            if marker in text:
                add_error(errors, f"Arbetsmarkör {marker!r} finns kvar i {path.relative_to(root)}")

    if numbers:
        expected = list(range(1, max(numbers) + 1))
        if numbers != expected:
            add_error(errors, f"Kapitelserien har luckor eller fel ordning: {numbers}, väntat {expected}")

    for rel, expected in {
        "README.md": "Erland Lindmark",
        "roman-bibel.md": "Erland Lindmark",
        "project-index.md": "När planen spricker",
        "projektstatus.md": "GitHub Actions",
    }.items():
        text = (root / rel).read_text(encoding="utf-8")
        if expected not in text:
            add_error(errors, f"{rel} saknar förväntad text: {expected!r}")

    validate_markdown_links(root, errors)

    if errors:
        print(f"Validering misslyckades med {len(errors)} fel.", file=sys.stderr)
        return 1

    print(f"OK: projektet validerades. {len(chapters)} kapitel hittades.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
