# EPUB/PDF-metadata

## Grundmetadata

- Titel: När planen spricker
- Undertitel: En roman om förändring, tillit och nya roller
- Författare: Erland Lindmark
- Språk: sv-SE
- Genre: realistisk arbetsplatsroman med romantisk subplot
- Målgrupp: vuxen
- Kapitelkälla: `kapitel/kapitel-01.md` till `kapitel/kapitel-23.md`
- Kapitelordning: numerisk ordning
- Omslag: `omslag/nar-planen-spricker-omslag.png`
- Exportstatus: Underlag komplett för Pandoc-baserad EPUB/PDF-export

## GitHub Actions

- Validering: `python3 scripts/validate_project.py .`
- Bygge: `python3 scripts/build_book.py --output-dir <utdatakatalog>`
- Preview-artifact: `nar-planen-spricker-preview`
- Release: triggas av `v*`-taggar

## Öppna val inför revision

- Avgör om Kapitel 23 ska behållas som epilog eller om romanen ska sluta vid Kapitel 22.
- Eventuellt ISBN/förlag saknas och är inte nödvändigt för teknisk export.
