#!/usr/bin/env python3
"""Bygg EPUB och PDF från Romanskaparprojektets kanoniska Markdown-kapitel.

Kapitelfilerna behålls oförändrade i `kapitel/`. Vid export skapas temporära
normaliserade kapitel där rubriken `# Kapitel N – Titel` blir `# N. Titel` och
kapitelnoteringar tas bort.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

PANDOC_VERSION = "3.1.11.1"
XHTML_NS = "http://www.w3.org/1999/xhtml"
EPUB_NS = "http://www.idpf.org/2007/ops"
OPF_NS = "http://www.idpf.org/2007/opf"
CHAPTER_H1_RE = re.compile(r"^#\s+Kapitel\s+(\d+)\s+[–-]\s+(.+?)\s*$")


def simple_metadata(path: Path) -> dict[str, str]:
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


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")


def pandoc_version() -> str:
    result = subprocess.run(["pandoc", "--version"], text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError("Pandoc finns inte i PATH.")
    first = result.stdout.splitlines()[0]
    match = re.search(r"pandoc\s+([0-9][^\s]*)", first)
    return match.group(1) if match else first


def strip_chapter_notes(text: str) -> str:
    patterns = [
        r"\n---\s*\n\s*Kort kapitelnotering:\s*\n[\s\S]*$",
        r"\n---\s*\n\s*##\s*Kapitelnotering\s*\n[\s\S]*$",
        r"\n---\s*\n\s*##\s*Efter kapitel\s*\n[\s\S]*$",
    ]
    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text.rstrip() + "\n"


def normalize_chapter(src: Path, dst: Path) -> tuple[int, str]:
    text = strip_chapter_notes(src.read_text(encoding="utf-8"))
    lines = text.splitlines()
    first_idx = next((i for i, line in enumerate(lines) if line.strip()), None)
    if first_idx is None:
        raise RuntimeError(f"Tom kapitelfil: {src}")
    match = CHAPTER_H1_RE.match(lines[first_idx].strip())
    if not match:
        raise RuntimeError(f"Kapitlet saknar väntad H1-rubrik: {src}")
    number = int(match.group(1))
    title = match.group(2).strip()
    lines[first_idx] = f"# {number}. {title}"
    dst.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return number, title


def prepare_chapters(root: Path, temp: Path) -> list[Path]:
    out_dir = temp / "chapters"
    out_dir.mkdir()
    normalized: list[Path] = []
    for src in sorted((root / "kapitel").glob("kapitel-[0-9][0-9].md")):
        dst = out_dir / src.name
        normalize_chapter(src, dst)
        normalized.append(dst)
    return normalized


def validate_epub(path: Path, expected_chapters: int, title: str) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            raise RuntimeError("EPUB-fel: mimetype ligger inte först.")
        if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise RuntimeError("EPUB-fel: mimetype är komprimerad.")

        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = container.find(
            ".//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile"
        )
        if rootfile is None:
            raise RuntimeError("EPUB-fel: OPF-root saknas.")
        opf_name = rootfile.attrib["full-path"]
        opf = ET.fromstring(archive.read(opf_name))
        ns = {"opf": OPF_NS}
        manifest = opf.find("opf:manifest", ns)
        spine = opf.find("opf:spine", ns)
        if manifest is None or spine is None:
            raise RuntimeError("EPUB-fel: manifest/spine saknas.")

        nav_item = next(
            (
                item for item in manifest.findall("opf:item", ns)
                if "nav" in item.attrib.get("properties", "").split()
            ),
            None,
        )
        if nav_item is None:
            raise RuntimeError("EPUB-fel: nav.xhtml saknas i manifestet.")

        nav_path = (Path(opf_name).parent / nav_item.attrib["href"]).as_posix()
        nav_root = ET.fromstring(archive.read(nav_path))
        nav_ns = {"x": XHTML_NS, "epub": EPUB_NS}
        anchors = nav_root.findall(".//x:nav[@epub:type='toc']//x:a", nav_ns)
        labels = ["".join(anchor.itertext()).strip() for anchor in anchors]
        chapter_labels = [label for label in labels if re.match(r"^\d+\.\s", label)]
        if len(chapter_labels) != expected_chapters:
            raise RuntimeError(
                f"EPUB-fel: TOC har {len(chapter_labels)} kapitelposter, väntat {expected_chapters}."
            )
        if title in labels:
            raise RuntimeError("EPUB-fel: titelsidan finns felaktigt med i TOC.")


def find_font_dir() -> Path | None:
    required = {
        "texgyrepagella-regular.otf",
        "texgyrepagella-bold.otf",
        "texgyrepagella-italic.otf",
        "texgyrepagella-bolditalic.otf",
    }
    for candidate in [
        Path("/usr/share/texmf/fonts/opentype/public/tex-gyre"),
        Path("/usr/share/fonts/opentype/texgyre"),
        Path("/usr/share/fonts/opentype/tex-gyre"),
    ]:
        if all((candidate / name).is_file() for name in required):
            return candidate
    for base in (Path("/usr/share/texmf"), Path("/usr/share/fonts")):
        if not base.exists():
            continue
        for regular in base.rglob("texgyrepagella-regular.otf"):
            candidate = regular.parent
            if all((candidate / name).is_file() for name in required):
                return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--name", default="")
    parser.add_argument("--formats", default="epub,pdf", help="Kommaseparerade format: epub,pdf")
    parser.add_argument("--allow-pandoc-version-mismatch", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output_dir = Path(args.output_dir).resolve()

    validation = subprocess.run([sys.executable, "scripts/validate_project.py", "."], cwd=root)
    if validation.returncode != 0:
        return validation.returncode

    version = pandoc_version()
    if version != PANDOC_VERSION and not args.allow_pandoc_version_mismatch:
        print(
            f"ERROR: Pandoc {PANDOC_VERSION} krävs för reproducerbart bygge; hittade {version}.",
            file=sys.stderr,
        )
        return 2

    metadata = simple_metadata(root / "publishing/metadata.yaml")
    title = metadata["title"]
    subtitle = metadata.get("subtitle", "")
    author = metadata["author"]
    cover = root / metadata.get("cover-image", "").replace("../", "", 1)
    base_name = args.name or slugify(title)
    base_name = re.sub(r"\.(epub|pdf)$", "", base_name, flags=re.IGNORECASE)
    formats = [item.strip().lower() for item in args.formats.split(",") if item.strip()]
    invalid = sorted(set(formats) - {"epub", "pdf"})
    if invalid or not formats:
        print("ERROR: --formats måste innehålla epub och/eller pdf.", file=sys.stderr)
        return 2

    output_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="roman-build-") as tmp_name:
        temp = Path(tmp_name)
        chapters = prepare_chapters(root, temp)

        title_page = temp / "00-title.md"
        subtitle_html = f'<p class="subtitle">{subtitle}</p>\n' if subtitle else ""
        title_page.write_text(
            '<section class="title-page">\n'
            f'<p class="book-title">{title}</p>\n'
            f'{subtitle_html}'
            f'<p class="author">{author}</p>\n'
            '</section>\n',
            encoding="utf-8",
        )

        if "epub" in formats:
            output = output_dir / f"{base_name}.epub"
            command = [
                "pandoc",
                str(title_page),
                *[str(path) for path in chapters],
                "--from=markdown+raw_html",
                "--to=epub3",
                "--output", str(output),
                "--metadata-file", str(root / "publishing/metadata.yaml"),
                "--css", str(root / "publishing/epub.css"),
                "--epub-cover-image", str(cover),
                "--epub-title-page=false",
                "--toc",
                "--toc-depth=1",
                "--split-level=1",
            ]
            subprocess.run(command, cwd=root, check=True)
            subprocess.run(
                [
                    sys.executable,
                    str(root / "publishing/fix-epub-after-pandoc.py"),
                    str(output),
                ],
                cwd=root,
                check=True,
            )
            validate_epub(output, len(chapters), title)
            print(f"OK: EPUB skapad och verifierad: {output}")

        if "pdf" in formats:
            if shutil.which("xelatex") is None:
                print("ERROR: xelatex krävs för PDF-bygget.", file=sys.stderr)
                return 2
            pdf = output_dir / f"{base_name}.pdf"
            font_dir = find_font_dir()
            font_args = ["--variable", f"pdf-font-dir={font_dir.as_posix()}"] if font_dir else []
            command = [
                "pandoc",
                *[str(path) for path in chapters],
                "--from=markdown",
                "--to=pdf",
                "--pdf-engine=xelatex",
                "--output", str(pdf),
                "--metadata-file", str(root / "publishing/metadata.yaml"),
                "--template", str(root / "publishing/pdf-template.tex"),
                "--lua-filter", str(root / "publishing/pdf-filter.lua"),
                *font_args,
                "--variable", f"cover-image-pdf={cover.as_posix()}",
                "--top-level-division=chapter",
            ]
            subprocess.run(command, cwd=root, check=True)
            if not pdf.exists() or pdf.stat().st_size < 10_000:
                print("ERROR: PDF-bygget gav ingen giltig PDF-fil.", file=sys.stderr)
                return 2
            print(f"OK: PDF skapad: {pdf}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
