# Project Index

## Projekt
- Titel: När planen spricker
- Senast uppdaterad: 2026-08-13
- Nuvarande fas: Första helutkast komplett med epilog / omslag inlagt / GitHub Actions-publicering införd / revision nästa
- Senast godkända kapitel: Inget formellt godkänt; kapitel 1–23 finns som utkast
- Nästa kapitel: Helhetsrevision

## Kapitelinventering
| Kapitel | Fil | Titel | Status |
|---|---|---|---|
| 1 | kapitel/kapitel-01.md | Förändringsresan börjar med PowerPoint | Utkast skrivet |
| 2 | kapitel/kapitel-02.md | Roller i rörelse | Utkast skrivet |
| 3 | kapitel/kapitel-03.md | Det första utvecklingsområdet | Utkast skrivet |
| 4 | kapitel/kapitel-04.md | Backloggen som blev en kravspecifikation | Utkast skrivet |
| 5 | kapitel/kapitel-05.md | Erik gör en plan för att slippa kaos | Utkast skrivet |
| 6 | kapitel/kapitel-06.md | Juridiken säger nej, eller kanske vänta | Utkast skrivet |
| 7 | kapitel/kapitel-07.md | Standup med statusrapportering | Utkast skrivet |
| 8 | kapitel/kapitel-08.md | Kaffemaskinens styrgrupp | Utkast skrivet |
| 9 | kapitel/kapitel-09.md | Drift får veta sist igen | Utkast skrivet |
| 10 | kapitel/kapitel-10.md | Produktägare på prov | Utkast skrivet |
| 11 | kapitel/kapitel-11.md | Arkitekturen protesterar | Utkast skrivet |
| 12 | kapitel/kapitel-12.md | Nästan en middag | Utkast skrivet |
| 13 | kapitel/kapitel-13.md | Leveransen som skulle bevisa allt | Utkast skrivet |
| 14 | kapitel/kapitel-14.md | Någon måste äga misslyckandet | Utkast skrivet |
| 15 | kapitel/kapitel-15.md | Det svåra samtalet | Utkast skrivet |
| 16 | kapitel/kapitel-16.md | När juristen kom in i rummet | Utkast skrivet |
| 17 | kapitel/kapitel-17.md | Från krav till samtal | Utkast skrivet |
| 18 | kapitel/kapitel-18.md | Drift är inte slutet av kedjan | Utkast skrivet |
| 19 | kapitel/kapitel-19.md | Utvecklingsområdet väljer bort | Utkast skrivet |
| 20 | kapitel/kapitel-20.md | En demo utan teater | Utkast skrivet |
| 21 | kapitel/kapitel-21.md | Inte färdiga, men förändrade | Utkast skrivet |
| 22 | kapitel/kapitel-22.md | Efter sprinten | Utkast skrivet |
| 23 | kapitel/kapitel-23.md | Tre månader senare | Utkast skrivet |

## Kanoniska projektfiler
| Fil | Syfte | Status |
|---|---|---|
| README.md | Start och arbetsflöde | OK |
| roman-bibel.md | Centrala fakta | OK |
| synopsis.md | Handlingsöversikt | OK |
| kapitelplan.md | Kapitelplan och status | OK |
| projektstatus.md | Senaste status och nästa steg | OK |
| arbetslogg.md | Projektändringar | OK |
| tidslinje.md | Händelser i romanen | OK |
| kontinuitetsanteckningar.md | Fakta och öppna trådar | OK |

## Synkkontroll
- Kapitel i `kapitel/`: 23
- Senaste kapitel i `kapitelplan.md`: 23
- Senaste kapitel i `projektstatus.md`: 23
- Senaste kapitel i `arbetslogg.md`: 23
- Resultat: Synkad


## Exportunderlag

| Fil | Syfte | Status |
|---|---|---|
| exports/epub-metadata.md | Metadata och standardval för EPUB-export | OK |
| exports/exportlogg.md | Logg över exportförberedelser | OK |

## EPUB-kontroll
- Titel: När planen spricker
- Författare: Erland Lindmark
- Språk: svenska
- Kapitel i exportunderlag: 23
- Resultat: Underlag komplett


## Omslag

| Fil | Syfte | Status |
|---|---|---|
| `omslag/nar-planen-spricker-omslag.png` | Omslagsbild/framsida | Skapad och inlagd |

## Metadata

- Status för omslagsbild: Skapad och inlagd (`omslag/nar-planen-spricker-omslag.png`).


## Publiceringsfiler
| Fil | Syfte | Status |
|---|---|---|
| `.github/workflows/01-validate.yml` | Snabb validering på PR/push till main | OK |
| `.github/workflows/02-build-preview.yml` | Manuellt previewbygge av EPUB och PDF | OK |
| `.github/workflows/03-release.yml` | Releasebygge på v*-taggar | OK |
| `scripts/validate_project.py` | Projektvalidering för CI | OK |
| `scripts/build_book.py` | EPUB/PDF-bygge via Pandoc | OK |
| `publishing/metadata.yaml` | Metadata för export | OK |
| `publishing/epub.css` | EPUB-stilmall | OK |
| `publishing/pdf-template.tex` | PDF-mall | OK |
| `publishing/pdf-filter.lua` | PDF-kapitelrubrikfilter | OK |
| `publishing/fix-epub-after-pandoc.py` | EPUB-efterbearbetning | OK |

## GitHub Actions-synkkontroll
- `.github` på samma nivå som `README.md`: Ja
- Preview-artifact: `nar-planen-spricker-preview`
- Release-assets: EPUB och PDF separata filer
- Resultat: Synkad
