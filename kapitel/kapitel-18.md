# Kapitel 18 – Drift är inte slutet av kedjan

Annika Sjöberg hade en regel som hon aldrig skrivit ner, eftersom den då riskerade att bli ett styrdokument:

Om någon sa “det där tar vi med drift sen”, skulle hon andas in, räkna till tre och inte kasta närmaste whiteboardpenna.

Regeln hade tjänat henne väl i många år. Den hade räddat konferensrum, relationer och möjligen hennes anställning. Den hade också gjort att hon ibland log på ett sätt som fick människor att tro att hon höll med, när hon i själva verket genomförde ett privat katastrofscenario i huvudet.

Den här morgonen räckte inte tre sekunder.

“Vi tänkte bara”, sa Fanny, “att om vi får upp första versionen i testmiljön före lunch kan vi—”

“Testmiljön”, sa Jonas från stolen bredvid Annika, “är inte en magisk skog där saker växer om man önskar tillräckligt hårt.”

Fanny stannade mitt i meningen.

Rummet Framtiden var ovanligt fullt för att vara klockan åtta. På bordet låg utskrifter från Noras behovssamtal med handläggarna i region syd. På väggen satt Oskars tre arkitekturprinciper, Leylas juridiska gränser och Karins handskrivna lapp: *Liten, verklig, driftbar*. Erik hade lagt till en undertext dagen innan: *Alla tre orden räknas.*

Annika hade uppskattat det mer än hon tänkte säga.

Ändå satt de här nu.

Fanny hade kommit in med den sortens energi som uppstod när en utvecklare äntligen såg en möjlig väg genom ett problem. Nora hade fyllt på med de första antagandena från lärloggen. Karin hade börjat formulera vad som behövde prövas med handläggarna. Erik hade ritat upp ett enkelt flöde. Och sedan, nästan omärkligt, hade samtalet glidit från *vad behöver vi förstå?* till *hur snabbt kan vi få upp något?*

Det var inte illvilja. Det var värre än så.

Det var vana.

Annika såg på whiteboarden. Där stod:

**Prövning: tydliga kompletteringspunkter med situationsanpassade exempel**

Under det hade någon skrivit:

- första vy
- enkel loggning
- handläggarens val synligt
- spårbar formulering
- visa för Malin/Patrik
- testmiljö?

Frågetecknet efter testmiljö var litet. För litet.

“Jag säger inte att vi inte kan göra det”, sa Fanny och drog handen genom håret. “Jag säger bara att vi behöver något konkret att reagera på. Annars sitter vi och pratar om hypotetiska handläggarbehov tills kompletteringsflödet hinner gå i pension.”

“Det är inte konkret jag invänder mot”, sa Jonas. “Det är ordet bara.”

Erik lutade sig fram. “Vilket bara?”

“Bara få upp första versionen. Bara koppla på loggning. Bara använda befintlig testdata. Bara visa ett flöde. Bara stänga av om det blir fel.” Jonas räknade på fingrarna utan att höja rösten. “Varje bara är någon annans kväll.”

Karin ryckte till lite vid det sista.

Annika såg det. Karin hade blivit bättre på att inte försvara sig reflexmässigt, men skulden syntes fortfarande snabbt i ansiktet. Som om varje ny risk betydde att hon redan hade svikit någon.

“Det är därför vi tog in er nu”, sa Karin.

Jonas nickade. “Ja. Och det är bra. Men om ni tar in oss tidigt och sedan ändå pratar som om drift är sista steget, då blir vi bara tidiga vittnen.”

Det blev tyst.

Annika hade arbetat med Jonas länge nog för att veta när han var arg och när han var trött. Det här var trötthet. Den sortens trötthet som kom av åratal av sena överlämningar, brandkårsutryckningar och möten där någon förklarade att “det här måste tyvärr gå snabbt” som om driftens verklighet var en personlig åsikt.

Hon lade händerna på bordet.

“Kan vi backa ett steg?” frågade hon.

Alla vände sig mot henne.

Det hände fortfarande. Inte lika ofta som förr, men ofta nog för att hon märkte det: rummet såg på Jonas när drift skulle säga något tekniskt och på henne när något skulle samordnas, mildras eller göras hanterbart. Hon hade länge använt den rollen. Det var praktiskt att vara den som översatte mellan grupper, fångade upp missförstånd och skickade tre vänliga mejl där ett ärligt samtal borde ha funnits.

Men den nya piloten hade börjat göra den vanan besvärlig. Om Annika skulle vara en del av kedjan, inte kudden mellan kedjans länkar, behövde hon sluta göra friktionen osynlig.

“Vi behöver inte bara fråga hur lösningen ska kunna driftsättas”, sa hon. “Vi behöver fråga vad drift behöver lära sig samtidigt som ni lär er om behovet.”

Fanny satte sig långsamt. “Vad menar du?”

“Om vi ska pröva stöd för kompletteringspunkter behöver vi förstå mer än om handläggaren gillar vyn. Vi behöver veta hur funktionen beter sig när någon använder fel mall, när integrationen svarar långsamt, när loggningen misslyckas, när någon försöker ångra sig, när texten behöver följas upp i efterhand.” Annika pekade på tavlan. “Det är inte efterarbete. Det är en del av prövningen.”

Nora började skriva.

Karin såg på Annika med den där blicken hon hade fått på sistone när någon flyttade romanens verkliga handling en bit framåt utan att be om lov.

“Så driftbarhet är inte ett kriterium på slutet”, sa Karin. “Det är ett antagande vi prövar.”

“Ja”, sa Annika. “Och det behöver stå så.”

Erik reste sig, tog en penna och skrev längst ner på tavlan:

**Driftbarhet är ett antagande, inte en checklista efteråt.**

Jonas läste meningen. “Det där är nästan sant.”

“Vad saknas?” frågade Erik.

“Att någon måste få tid att göra något med antagandet.”

Fanny suckade, men inte av irritation. Mer som om kroppen släppte ifrån sig en gammal reflex.

“Jag hör er”, sa hon. “Men jag blir rädd att allt blir större igen. Vi började med en liten prövning för att inte fastna. Om vi lägger till alla tänkbara driftfrågor är vi tillbaka i ett förprojekt med tolv spår.”

“Bra”, sa Jonas. “Då har vi samma rädsla från olika håll.”

“Det var... ovanligt diplomatiskt.”

“Annika har coachat mig.”

“Jag har försökt”, sa Annika.

Karin log, men Erik såg fortfarande på tavlan. Annika såg hur han kämpade mot något. Inte mot Jonas eller Fanny, utan mot sin egen gamla kompetens. Hon kunde nästan höra planeringsmaskinen i honom starta: risklista, beroendekarta, aktivitetsplan, ansvarig, datum, status. Det var inte fel. Det var bara farligt när det blev reflex.

“Vi behöver avgränsa driftprövningen lika hårt som funktionsprövningen”, sa han till slut.

Karin vände sig mot honom.

“Tre frågor?” föreslog han. “Inte alla driftfrågor. Tre saker vi behöver veta för att våga gå vidare.”

Annika kände hur något i rummet lättade. Inte för att problemet blev enkelt, utan för att det fick kanter.

Jonas lutade sig bakåt. “Det kan jag leva med.”

“Vilka tre?” frågade Nora.

Annika tittade på Jonas. Han gjorde en liten gest som betydde att hon skulle börja.

Förr hade hon kanske bett honom ta den tekniska delen först. Nu lät hon bli.

“Ett”, sa hon. “Kan vi följa vad som hänt utan att skapa mer manuell kontroll? Alltså loggning som faktiskt hjälper handläggare, support och drift.”

Nora skrev.

“Två”, fortsatte Annika. “Kan vi införa stödet utan att skapa beroenden till nästa stora releasefönster? Om varje liten förbättring ändå måste vänta på samma gamla tåg har vi inte förändrat flödet.”

Jonas nickade. “Och tre: kan vi backa eller begränsa funktionen utan att behöva nattjobba, ringa åtta personer och hoppas att någon minns hur konfigurationen fungerar?”

Fanny pekade på honom. “Den där vill jag också ha.”

“Utvecklare tycker också om att sova?” sa Mats från dörren.

Ingen hade hört honom komma in. Det var Mats främsta organisatoriska förmåga: han materialiserades när någon började bli för abstrakt.

“Du är sen”, sa Karin.

“Jag är verksamhetsnära. Vi kommer när verkligheten har hunnit ikapp.”

Han satte sig bredvid Nora och tittade på tavlan.

“Det där gillar jag”, sa han och nickade mot de tre punkterna. “Särskilt sova-delen.”

“Det är inte den officiella formuleringen”, sa Erik.

“Den borde vara det. *Målbild: handläggare får stöd och ingen behöver nattjobba av dumma skäl.* Jag skulle läsa den strategin.”

Karin skrattade, men hon skrev ändå ner något i sitt block.

Annika såg på gruppen och kände en försiktig, nästan ovälkommen värme. Det här var det hon länge hade försökt ordna med mejltrådar, mötesanteckningar och förklarande samtal i korridorer. Inte harmoni. Något bättre: friktion medan alla fortfarande satt kvar.

Då ringde Eriks telefon.

Han tittade på skärmen och blev stilla.

“Birgitta”, sa han.

Rummet förändrades. Inte mycket. Men tillräckligt.

Karin såg på honom. Det fanns fortfarande en skörhet mellan dem efter det som hänt med demon. De hade börjat hitta tillbaka professionellt, men varje samtal uppåt bar på en gammal risk: att Erik skulle gå före, översätta, skydda, rädda. Eller att Karin skulle förvänta sig att han gjorde det och sedan hata honom för det.

Erik höll telefonen i handen tills samtalet nästan gick till svararen.

“Jag tar den här i rummet”, sa han.

Det var en liten mening. Annika undrade om alla förstod hur stor den var.

Karin nickade.

Erik svarade och satte på högtalare.

“Erik Sand.”

“Hej Erik, det är Birgitta. Har du två minuter?”

Birgitta Ahls röst hade den särskilda klarhet som människor fick när de visste att två minuter betydde sju och att båda parter förväntades låtsas något annat.

“Jag sitter med Karin och delar av området”, sa Erik. “Vi arbetar med nästa prövning. Du är på högtalare.”

En sekunds tystnad.

“Jaha”, sa Birgitta. “Bra. Då kanske det är ännu bättre.”

Karin lutade sig fram. “Hej Birgitta.”

“Hej Karin. Jag ville bara stämma av hur det går med att få fram något mer konkret efter förra veckans... lärdomar.”

Mats tittade ner i bordet med en min som sa att *lärdomar* var en tapper omskrivning.

“Vi arbetar med en liten prövning kring kompletteringspunkter”, sa Karin. “Utifrån behovssamtalen med region syd.”

“Bra”, sa Birgitta. “Och när kan vi visa att den faktiskt går att leverera?”

Karin öppnade munnen, men Erik hann nästan svara. Annika såg rörelsen. Han hejdade sig. Bara ett ögonblick, men tillräckligt för att Karin skulle märka det.

Hon tog över.

“Vi kan visa nästa vecka vad vi har lärt oss om funktion, rättssäkerhet och driftbarhet”, sa hon. “Inte lova produktionssättning.”

“Jag förstår skillnaden”, sa Birgitta, på ett sätt som gjorde det oklart om hon uppskattade den.

“Bra”, sa Karin. “För den är viktig.”

Annika såg Jonas lyfta blicken. Fanny slutade snurra pennan mellan fingrarna.

Birgitta fortsatte:

“Jag får frågor från ledningen om piloten återhämtat sig. De behöver känna att vi inte bara analyserar.”

“Det behöver vi också”, sa Karin. “Därför prövar vi på riktigt. Men om vi pressar in något i en miljö utan att veta om det går att följa, begränsa och drifta, då har vi inte återhämtat oss. Då upprepar vi bara felet med bättre rubrik.”

Erik såg på Karin. Inte stolt den här gången. Eller jo, kanske. Men mest koncentrerat, som om han höll fast vid att hans roll just nu var att inte fylla tystnaden.

Birgitta var tyst några sekunder.

“Vem äger den bedömningen?” frågade hon.

Det var en gammal fråga i ny kostym. Vem kan vi hålla ansvarig? Vem kan vi ringa om detta blir pinsamt? Vem står på raden i protokollet?

Karin andades in.

“Jag äger prioriteringen av värde och prövningens omfattning”, sa hon. “Leyla äger inte juridiken men hjälper oss hålla gränserna tydliga. Jonas och Annika äger inte hela driftsfrågan men synliggör vad vi måste kunna för att gå vidare. Fanny och teamet äger inte verksamhetens behov men kan visa vad som är tekniskt möjligt. Erik hjälper oss hålla ihop ansvaren utan att flytta dem till sig.”

Erik såg ner på bordet.

Annika fick en oväntad klump i halsen. Inte för att formuleringen var perfekt. Det var den inte. Men för att drift inte hade hamnat sist. Inte som leveransmottagare. Inte som kvittens. Som en del av ansvarsväven.

“Det där var ett långt svar”, sa Birgitta.

“Ja”, sa Karin. “Det beror på att det gamla korta svaret inte fungerade.”

Mats lade handen över munnen.

Birgitta suckade, men det fanns något annat i sucken än irritation. Kanske trött respekt.

“Skicka en kort lägesbild i eftermiddag”, sa hon. “Med de tre driftbarhetsfrågorna och vad ni kan visa nästa vecka. Kort, Karin.”

“En sida”, sa Karin.

“En halv.”

“En sida med luft.”

“Jag går med på luft.”

Samtalet avslutades.

Rummet var tyst i tre sekunder.

Sedan sa Mats: “En sida med luft är den mest hoppfulla förhandlingen jag hört på den här myndigheten.”

Fanny skrattade. Jonas också, kort och överraskat.

Karin lutade sig tillbaka och slöt ögonen en sekund. När hon öppnade dem såg hon på Erik.

“Tack för att du tog samtalet här.”

Han stoppade undan telefonen. “Ny teamregel. Inga alternativa vägar.”

“Det där var inte bara regel”, sa hon.

“Nej.”

De sa inget mer. De behövde inte. Annika såg blicken mellan dem och valde att inte tolka den högt, vilket hon ansåg vara en tjänst till både romanen och arbetsmiljön.

“Då gör vi så här”, sa hon och drog tillbaka rummet till tavlan innan någon hann bli generad. “Tre driftbarhetsfrågor. En liten prövning. Ingen produktionsromantik.”

“Produktionsromantik?” sa Fanny.

“Det är när någon blir förälskad i tanken på att gå live innan relationen är mogen”, sa Mats.

“Jag vill aldrig höra dig säga relationen är mogen igen”, sa Karin.

“Noterat.”

De arbetade i nästan två timmar.

Inte effektivt på det sätt som såg bra ut i en rapport. De backade, strök, ritade om. Fanny insåg att en del av stödet kunde byggas som konfigurerbar textstruktur i stället för hårdkodad logik. Jonas visade varför en till synes enkel loggpost behövde innehålla både ändring, användare, tidpunkt och sammanhang för att vara användbar vid felsökning och uppföljning. Nora justerade lärloggen så att varje antagande kopplades till både handläggarbehov och driftbarhetsfråga. Mats protesterade när språket blev för tekniskt. Karin höll fokus på vad handläggarna faktiskt skulle kunna göra annorlunda. Erik ritade bara när någon bad honom.

Det sista märkte Annika.

Han stod med pennan i handen flera gånger. Men han väntade. Ibland för länge, så att Fanny till slut sa “Erik, kan du rita det där du försöker låta bli att rita?” och han gjorde det med en min som om han blivit avslöjad i en ofarlig men pinsam last.

Vid elva kom Leyla in, fem minuter sen och med en kopp te som doftade mynta.

“Jag fick er lägesbildsutkast”, sa hon. “Jag har tre invändningar och en komplimang.”

“Börja med komplimangen”, sa Mats. “Vi är sköra.”

“Ni har inte beskrivit juridik som godkännande på slutet.”

“Det var en bra komplimang”, sa Karin.

“Och invändningarna?” frågade Erik.

Leyla pekade på tavlan. “Om ni loggar handläggarens val måste ni vara tydliga med syfte. Är loggen till för driftfelsökning, rättslig spårbarhet, verksamhetsuppföljning eller allt på en gång? Allt på en gång brukar betyda att ingen har tänkt.”

Jonas nickade direkt. “Tack.”

Fanny såg på honom. “Du blev glad av en invändning.”

“En tidig invändning”, sa Jonas. “Det är skillnad.”

Annika log.

Där var det. Inte det stora genombrottet. Inte den inspirerande transformationen med soluppgång. Bara en drifttekniker som blev glad över att en jurist invände innan någon byggt fel sak.

Karin skrev på tavlan:

**Tidiga invändningar är framdrift.**

“Den där kommer någon sätta på en mugg”, sa Mats.

“Då säger jag upp mig”, sa Leyla.

När de till slut stängde mötet hade de inte en färdig lösning. De hade något bättre än förra gången: en prövning som gick att förstå, begränsa och säga nej till om den inte höll.

Annika stannade kvar för att fotografera tavlan. Jonas hjälpte henne samla ihop några sladdar som ingen visste vem som ägde men alla var rädda att kasta.

“Du sa mycket i dag”, sa han.

“För mycket?”

“Nej.” Han drog ihop sladdarna i en knut som skulle få alla framtida människor att hata honom. “Lagom för att vara du. För lite för att vara nödvändigt på sikt.”

Hon såg på honom.

“Vad betyder det?”

“Att du fortfarande översätter åt oss andra när vi borde lära oss språket själva.”

Det stack till. Inte för att han hade fel.

Annika hade byggt en yrkesroll på att förstå mellanrummen. Hon visste vem som behövde ringas innan mötet, vem som behövde en mildare formulering, vilken drifttekniker som skulle säga nej men mena “förklara bättre”, vilken chef som behövde känna sig informerad för att inte börja styra. Hon hade varit stolt över det.

Hon var fortfarande stolt.

Men hon började se priset. När hon bar mellanrummen slapp andra kliva över dem.

“Jag vet”, sa hon.

Jonas nickade. “Bra.”

Det var Jonas version av omsorg.

Karin kom tillbaka in just när han gick. Hon hade telefonen i handen.

“Jag skickar lägesbilden om tio minuter”, sa hon. “Vill du läsa driftavsnittet?”

Förr skulle Annika ha sagt ja direkt, putsat formuleringarna, mjukat upp Jonas kanter och sett till att ingen kunde missförstå.

Nu tänkte hon på vad han nyss sagt.

“Nej”, sa hon.

Karin stannade.

Annika kände hur reflexen att förklara sig steg, men hon lät den inte ta över.

“Skicka den som du har förstått den”, sa hon. “Om du har missförstått något tar vi det öppet. Annars lär du dig bara att alltid gå via mig.”

Karin såg på henne länge.

Sedan log hon långsamt. “Det där var väldigt agilt av dig.”

“Jag vet. Jag behöver sätta mig ner.”

“Det finns stolar.”

“Jag menar emotionellt.”

Karin skrattade, och Annika kände att något litet men bestämt hade flyttat sig.

När hon senare gick tillbaka mot driftens rum passerade hon kaffemaskinen. Den blinkade rött, som vanligt. På en lapp ovanför hade någon skrivit: *Felanmälan är gjord. Sluta starta egna initiativ.*

Annika tog en bild och skickade den till Jonas.

Han svarade efter en minut:

*Agilt kaffe. Minimal fungerande besvikelse.*

Hon skrattade högt i korridoren.

Det var inte mycket. En tavla, tre frågor, en lägesbild med luft, en produktägare som inte rundade drift, en utvecklingsområdesansvarig som tog samtalet i rummet, en jurist som invände i tid och en driftkoordinator som lät bli att översätta åt alla.

Men när Annika kom fram till driftens rum kändes kedjan för första gången inte som något som började någon annanstans och slutade hos dem.

Den gick genom dem.

Och vidare.
