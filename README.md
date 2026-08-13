# Romanprojekt – När planen spricker

Författare: Erland Lindmark

Detta är projektarkivet för romanen som utvecklas steg för steg tillsammans med Romanskaparen.

## Arbetsflöde

1. Planera romankärnan: huvudperson, mål, hinder, insats och förändring.
2. Skapa synopsis, kapitelplan, romanbibel och stilguide.
3. Skriv ett kapitel i taget i chatten.
4. Justera kapitlet tills det är godkänt.
5. Uppdatera projektfilerna och projektstatus.
6. Fortsätt med nästa kapitel eller revision.

## Viktiga filer

- `projektstatus.md` visar nuvarande fas, senaste godkända kapitel och nästa rekommenderade steg.
- `roman-bibel.md` innehåller projektets centrala fakta.
- `synopsis.md` sammanfattar hela handlingen.
- `kapitelplan.md` är färdplanen för romanen.
- `stilguide.md` håller språk, ton och perspektiv konsekvent.
- `tidslinje.md` håller ordning på händelser i romanen.
- `kontinuitetsanteckningar.md` fångar fakta som inte får motsägas.
- `arbetslogg.md` visar vad som har gjorts.
- `kapitel/` innehåller kapitelutkast och godkända kapitel.


## Omslag

- Omslagsbild: `omslag/nar-planen-spricker-omslag.png`
- Status: Skapad och inlagd i projektarkivet 2026-05-26.
- Bilden visar ett stilrent, nordiskt myndighets-/kontorsomslag med titel, undertitel och författarnamn.


## GitHub Actions och publicering

Projektet innehåller nu ett GitHub Actions-upplägg på repository-rotnivå:

- `.github/workflows/01-validate.yml` validerar projektstruktur, metadata, omslag och kapitelserie.
- `.github/workflows/02-build-preview.yml` bygger EPUB och PDF manuellt som ett gemensamt preview-artifact.
- `.github/workflows/03-release.yml` bygger EPUB och PDF vid `v*`-taggar och laddar upp dem som separata release assets.

Publiceringsfilerna ligger i:

- `scripts/validate_project.py`
- `scripts/build_book.py`
- `publishing/metadata.yaml`
- `publishing/epub.css`
- `publishing/fix-epub-after-pandoc.py`
- `publishing/pdf-template.tex`
- `publishing/pdf-filter.lua`

`.github` ligger på samma nivå som denna `README.md`.


## PDF-previewmall

PDF-mallen i `publishing/pdf-template.tex` är åtgärdad 2026-08-13 så GitHub Actions Preview inte ska skapa en tom sida före omslaget eller före innehållsförteckningen.
