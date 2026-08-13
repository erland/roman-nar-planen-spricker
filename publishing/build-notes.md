# Build notes

Markdown-kapitlen i `kapitel/` är kanonisk källa. GitHub Actions bygger exporter från faktiska kapitel i numerisk ordning.

## GitHub Actions-införande

- Datum: 2026-08-13
- Källa för koncept: bifogat Romanskaparen GitHub Actions publiceringskit
- Anpassat projekt: När planen spricker
- Författare: Erland Lindmark
- Kapitelkälla: `kapitel/kapitel-01.md`–`kapitel/kapitel-23.md`
- Omslag: `omslag/nar-planen-spricker-omslag.png`
- Metadata: `publishing/metadata.yaml`
- Byggscript: `scripts/build_book.py`
- Validering: `scripts/validate_project.py`
- Pandoc-version i CI: 3.1.11.1

## Workflows

- `.github/workflows/01-validate.yml`: kör snabb projektvalidering på pull request och push till `main`.
- `.github/workflows/02-build-preview.yml`: manuellt bygge av EPUB och PDF, publicerade i ett gemensamt artifact: `nar-planen-spricker-preview`.
- `.github/workflows/03-release.yml`: bygger EPUB och PDF vid `v*`-tagg och laddar upp dem som separata GitHub Release assets.

## Exportprinciper

- Kapitelnoteringar exporteras inte.
- Rubriker normaliseras temporärt från `# Kapitel N – Titel` till `# N. Titel` för Pandoc.
- Projektets källkapitel ändras inte av byggscriptet.
- EPUB får omslag, titelsida och navigerbar innehållsförteckning.
- PDF får helsidesomslag, separat titelsida och synlig innehållsförteckning.
