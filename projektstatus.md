# Projektstatus

## Nuvarande fas

Första helutkast komplett med epilog / omslag inlagt / GitHub Actions-publicering införd / revision nästa.


## Senast godkända kapitel eller del

- Senast godkända: Inget kapitel formellt godkänt; kapitel 1–23 finns som utkast.
- Senast ändrad: Kapitel 23 – Tre månader senare, utkast skrivet.

## Nästa rekommenderade steg

Kör helhetsrevision, eller lägg projektet i ett GitHub-repository och kör Validate/Build Preview för att skapa EPUB/PDF via Actions.


## Viktiga öppna beslut

- Ska myndigheten heta Myndigheten för Samhällstjänster i själva romantexten eller förbli namnlös?
- Hur tydligt ska XLPM nämnas i dialog och narration i slutlig version?
- Ska “femfrågorna” få större plats som återkommande motiv i revisionen?
- Ska romance-spåret förstärkas i tidigare kapitel så slutmiddagen känns ännu mer intjänad?
- Kapitel 23 fungerar nu som epilog; vid revision bör vi avgöra om romanen ska sluta vid Kapitel 22 eller behålla epilogen som Kapitel 23.

## Risker att bevaka

- Romanen får inte bli en metodhandbok.
- För många roller kan göra berättelsen spretig.
- Romance-spåret ska byggas långsamt och vuxet, utan att ta över arbetsplatsromanen.
- Agilt arbetssätt ska visas genom konflikter, val och konsekvenser, inte förklaras som teori.
- Ledningens intresse för teamets arbetssätt får inte bli för enkel framgång; det ska fortsatt kännas som en realistisk risk för mallifiering.
- Slutet ska vara hoppfullt men inte orealistiskt perfekt.

## Kontinuitet som måste följas upp vid revision

- Karin har tackat ja till produktägarrollen och utvecklats från att vilja göra alla nöjda till att kunna välja bort och stå kvar.
- Erik har tackat ja till pilotens områdesledning/utvecklingsområdesansvar och utvecklats från kontrollbärare till möjliggörare.
- Pilotområdet har valt första fokus: att minska fel och dubbelarbete i handläggarnas kompletteringsflöde.
- Backloggen innehåller lärandeinriktade poster, inte en komplett kravkatalog.
- Driftbarhetskriterierna är prioriterade som del av första steget.
- Oskars arkitekturprinciper gäller för kompletteringsflödet.
- Handläggarstödet är bortvalt som byggsteg, men hålls synligt genom lärdatum och planerade behovssamtal.
- Formuleringen “Vi lovar inte datum för sådant vi ännu inte förstår. Vi lovar när vi ska förstå mer.” har etablerats.
- Femfrågorna från Kapitel 21 är ett stöd för lärande, men riskerar att bli en ny mall.
- Karin och Erik har erkänt känslor, tagit relationen långsamt och går i Kapitel 22 på en riktig middag.
- Teamet har öppet adresserat att Karin och Eriks relation inte får påverka prioriteringar, ansvar eller förtroende.
- Slutformuleringar från Kapitel 22: “Mindre teater. Mer verklighet.” och “Vi fortsätter.”
- Kapitel 23 hoppar tre månader framåt och visar att teamet fortsätter upptäcka missförstånd tidigt; slutfrågan är “Vad har vi missförstått den här gången?”

## Användarens aktuella önskemål

- Kapiteltexterna behöver inte visas i chatten när zipen uppdateras.
- Berättelsen ska fortsätta vara realistisk, varm, humoristisk och lite romantisk.
- Mer känslomässigt djup är önskat än bara korta dialogfraser.


## EPUB/PDF-status

Underlaget för att skapa EPUB och PDF via Pandoc/GitHub Actions är komplett med följande standardval:

- Titel: När planen spricker
- Undertitel: En roman om förändring, tillit och nya roller
- Författare: Erland Lindmark
- Språk: sv-SE
- Kapitel: 1–23 i numerisk ordning
- Omslag: `omslag/nar-planen-spricker-omslag.png`
- Kapitel 23 behandlas som epilog/bonuskapitel och inkluderas vid export om inget annat beslutas.

Nästa exportsteg är att köra `python3 scripts/build_book.py --output-dir <utdatakatalog>` lokalt eller via GitHub Actions Build Preview.

## Omslagsbild

- Status: Skapad och inlagd som `omslag/nar-planen-spricker-omslag.png`.


## GitHub Actions-status

- Infört: 2026-08-13
- `.github/` ligger på samma nivå som `README.md`.
- Validate-workflow finns för pull request och push till `main`.
- Build Preview-workflow finns för manuellt EPUB/PDF-bygge.
- Release-workflow finns för `v*`-taggar.
- Bygget använder `scripts/build_book.py`, `scripts/validate_project.py` och filerna i `publishing/`.
- Preview-artifact: `nar-planen-spricker-preview`.
