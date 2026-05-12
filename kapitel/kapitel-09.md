# Kapitel 9 – Drift får veta sist igen

Jonas Eklund litade inte på ordet *bara*.

Det hade börjat som en yrkesmässig iakttagelse och med åren blivit något närmast filosofiskt. På myndigheten betydde *bara* sällan bara. *Vi ska bara lägga till en liten knapp* kunde innebära tre nya integrationer, två ändrade behörighetsflöden och en databasfråga som fick produktionsmiljön att hosta blod. *Det är bara en textändring* hade en gång lett till att sjuttontusen automatiska brev skickades med fel hänvisning till en paragraf som dessutom hade upphävts året innan.

Och *vi ska bara visa ett första enkelt stöd i kompletteringsflödet*?

Jonas stirrade på ärendet i driftens kö och kände hur nacken långsamt blev stel.

Det var torsdag morgon. Han hade egentligen tänkt ägna första timmen åt att följa upp en nattlig övervakningsvarning som visat sig vara både falsk och irriterande envis. I stället satt han i driftens rum med en skärm full av loggutdrag, en halvfull kaffemugg och en känsla av att någon någonstans hade sagt “det där tar vi sen”.

Rummet var inte gjort för framtidsvisioner. Det hade praktisk belysning, för många skärmar och ett litet fönster mot innergården där ventilationstrummorna såg ut att ha gett upp hoppet om mänskligheten. På väggen satt en utskriven lapp som någon hade tejpat upp efter en särskilt rörig release två år tidigare:

**Inget är klart förrän det går att drifta.**

Jonas hade inte skrivit den, men han hade låtit den sitta kvar.

“Du har den där minen”, sa Annika Sjöberg från skrivbordet bredvid.

“Vilken av dem?”

“Den där du försöker bestämma om du ska vara tyst eller förstöra någons dag.”

“Jag ser det mer som att förbättra någons verklighetskontakt.”

Annika rullade stolen närmare och tittade på hans skärm. Hon hade håret uppsatt med en penna som inte längre gick att skriva med, och hon bar alltid en anteckningsbok trots att hon samordnade mer i huvudet än de flesta gjorde i hela projektverktyg. Jonas hade arbetat med henne länge nog för att veta att hennes lugn inte betydde att hon var avslappnad. Det betydde att hon redan hade sett tre problem till.

“Är det piloten?” frågade hon.

“Det är kompletteringsstödet.”

“Det som skulle vara litet?”

“Bara litet.”

Annika suckade. “Där kom det.”

Jonas pekade på raden i loggutdraget. “De verkar vilja hämta realtidsdata från meddelandetjänsten när handläggaren öppnar stödvyn.”

“Det låter inte orimligt.”

“Nej. Om meddelandetjänsten svarar.”

“Gör den inte det?”

“Oftast.”

Annika såg på honom.

“Oftast är inget driftord”, sa han.

Hon lutade sig fram och läste mer noggrant. “Vad händer när den inte svarar?”

“Det finns ingen tydlig fallback.”

“Timeout?”

“För lång.”

“Felmeddelande?”

“Tekniskt.”

“Övervakning?”

Jonas pekade på en tom rad i dokumentet som skickats över från utveckling. “Här bor övervakningen. Den har ett vackert men outvecklat liv.”

Annika drog handen över ansiktet. “När fick vi det här?”

“I går 16.47.”

Hon sa inget. Det var värre än att svära.

Meddelandet hade kommit från Fanny, inte för att hon försökte smyga in något, utan för att hon äntligen själv fått ihop underlaget efter ett möte där någon insett att drift “kanske borde titta”. Jonas tyckte om Fanny. Hon var vass, snabb och kunde höra skillnad på tekniska invändningar och organisatoriskt gnäll. Men också hon hade formats av en miljö där drift ofta blev sista hållplatsen före produktion, en sorts tullstation där trötta människor lämnade in sina paket och hoppades att ingen skulle öppna dem.

“Demot är på onsdag”, sa Annika.

“Jag vet.”

“Ledningen kommer vara där.”

“Jag vet.”

“Karin kommer inte vilja få höra det här via bakvägen.”

Jonas lutade sig tillbaka. Stolen gnisslade på ett sätt som borde ha felanmälts 2021.

“Då får vi säga det rakt.”

“Till vem?”

Han tittade på klockan. “Alla.”

Annika höjde ögonbrynen. “Du menar ett möte.”

“Jag menar en incident som ännu inte inträffat.”

“Det är också ett möte.”

Han kunde inte låta bli att le.

Tjugo minuter senare satt de i ett rum som hette Utsikten men saknade fönster. Namnet hade länge varit föremål för driftens interna kommentarer, särskilt eftersom projektorn i rummet alltid behövde två försök innan den hittade rätt ingång. Den här gången fungerade den på första försöket, vilket Jonas tog som ett dåligt tecken. När tekniken uppförde sig i mötesrum brukade problemen ha flyttat någon annanstans.

Karin kom in först, med datorn under armen och den koncentrerade min hon fick när hon redan bar på tre samtal hon inte hunnit ha. Erik kom strax efter henne. Han stannade ett ögonblick i dörren, såg Jonas och Annika, såg skärmen, och Jonas kunde nästan följa hur hans hjärna började skapa struktur av hotet.

Fanny kom med en mugg te och satte sig utan att ta av jackan.

“Det här känns som en sådan samling där jag kommer få ångra något jag gjort”, sa hon.

“Vi är inte där än”, sa Annika.

“Tröstande.”

Nora kom sist, andfådd, med ett block fullt av lappar. “Förlåt. Jag var i samtal med två handläggare om stödtexterna och en av dem sa ‘det vore ju bra om systemet bara visste vad jag menar’, så jag behövde andas i trapphuset.”

“Alla behöver andas någon gång”, sa Fanny. “Vissa behov kräver mer syre än andra.”

Karin satte sig. “Okej. Vad har hänt?”

Jonas uppskattade frågan. Inte *är det ett problem?* Inte *kan vi ta det sen?* Bara vad har hänt.

Han gick fram till skärmen.

“Det korta svaret är att det första kompletteringsstödet inte är odriftbart”, sa han. “Men det är mer sårbart än ni tror.”

“Det där var ett driftmässigt sätt att säga att det är dåligt”, sa Fanny.

“Nej. Om det var dåligt skulle jag säga det.”

“Det skulle han”, sa Annika.

Jonas klickade fram den enkla skissen han och Annika gjort. Den var ful men begriplig: stödvyn, ärendeplattformen, meddelandetjänsten, loggning, övervakning, handläggarens vy. Pilarna gick åt flera håll, vilket alltid gjorde människor mer realistiska.

“Det ni vill visa på demot är ett stöd som hämtar information från meddelandetjänsten och hjälper handläggaren förstå om en komplettering är skickad, väntar eller behöver följas upp. Det är en bra idé. Men just nu bygger flödet på att meddelandetjänsten svarar snabbt och korrekt varje gång. När den inte gör det får handläggaren ett tekniskt fel eller en fördröjning som ser ut som att plattformen hängt sig.”

Karin blev alldeles stilla. “Hur ofta händer det?”

“Det beror på belastning, tidpunkt och om någon tittar argt på integrationen”, sa Jonas.

Fanny lutade sig fram. “Vi har testat mot testmiljön.”

“Jag vet.”

“Den svarade.”

“Testmiljön är som en hotellfrukost på konferens. Allt ser ordnat ut för att ingen bor där på riktigt.”

Fanny öppnade munnen, stängde den igen och pekade på honom med muggen. “Den där var oförskämt bra.”

Erik hade inte sagt något än. Det oroade Jonas lite. En tyst Erik Sand kunde vara ett tecken på att han lyssnade, men också på att han var på väg att bygga en räddningsplan med fem arbetsströmmar.

“Vad behöver vi göra?” frågade Erik.

Där var den.

Jonas klickade till nästa bild. “Ni behöver inte stoppa allt. Men ni behöver välja vad ni faktiskt vill lära er av demot.”

Karin såg upp. “Förklara.”

“Om syftet är att visa att vi kan bygga ett komplett tekniskt flöde, då är ni inte redo. Inte utan fallback, rimliga timeouts, användbart felmeddelande, loggning och övervakning. Om syftet är att lära er om handläggarnas behov och om stödlogiken hjälper dem, då kan ni visa det på ett kontrollerat sätt utan att låtsas att produktionsflödet är klart.”

Rummet blev tyst.

Jonas såg hur orden arbetade sig genom gruppen. Hos Fanny blev de först teknisk prövning, sedan lättnad och irritation i samma ansikte. Hos Nora blev de en fråga om vad de faktiskt skulle visa handläggarna. Hos Erik blev de en konflikt mellan att rädda leveransen och att låta den bli mindre. Hos Karin blev de något tyngre.

Hon hade sålt in demot uppåt, förstod han. Inte som färdig lösning, kanske, men som konkret framsteg. Hon hade sagt att de skulle visa något verkligt. Nu måste hon bestämma vad verkligt betydde.

“Vi har ledningsavstämning nästa torsdag”, sa hon.

“Jag vet”, sa Annika. “Det är därför vi säger det nu.”

“Det är sent.”

“Ja”, sa Jonas. “Men det är tidigare än produktion.”

Karin tog emot det utan att värja sig. Jonas såg respekt för henne växa i rummet just då. Inte för att hon hade en lösning, utan för att hon inte omedelbart försökte lägga ansvaret någon annanstans.

Erik lutade sig fram. “Kan vi dela upp det? Visa stödlogiken med simulerade statusar i demo, samtidigt som vi skapar en teknisk åtgärdslista för driftbarhet innan någon pratar om produktionssättning.”

“Ja”, sa Jonas. “Om ni är tydliga med att det är just det.”

“Och om ingen säger ‘nästan klart’”, sa Annika.

Fanny gjorde en grimas. “Jag hatar nästan klart.”

“Alla hatar nästan klart”, sa Jonas. “Nästan klart är bara inte klart med bättre självförtroende.”

Nora bläddrade bland sina papper. “Men om vi visar simulerade statusar, kommer handläggarna förstå vad de testar?”

“Det är där du kommer in”, sa Karin.

Nora såg först skrämd ut, sedan fokuserad.

“Vi kan formulera det som tre situationer”, sa hon långsamt. “Handläggaren ser ett ärende där komplettering är skickad, ett där svar saknas och ett där något behöver följas upp. Vi testar om stödet hjälper dem fatta nästa steg. Inte om integrationen fungerar.”

“Precis”, sa Jonas.

Fanny nickade, nu snabbare. “Då kan jag bygga om demovyn så den tydligt visar att statusarna är styrda för test. Och vi kan lägga in ett fel-läge också.”

“Ett fel-läge?” frågade Erik.

“Ja. Om vi ändå ska lära oss kan vi visa vad handläggaren behöver se när systemet inte vet. Det är bättre än att låtsas att system alltid vet.”

Karin såg på Fanny, och något i hennes ansikte ljusnade. “Det där är bra.”

“Jag vet”, sa Fanny, men hon lät nöjd snarare än stöddig.

Erik hade tagit fram sin penna. Jonas såg det och kände hur kroppen förberedde sig på en lista. Det var inte listor han var emot. Det var listor som skapades för att lugna någon och sedan dumpades på dem som redan var sena.

“Vi behöver tre spår”, sa Erik. “Demo för lärande. Teknisk driftbarhet. Kommunikationslinje uppåt.”

Karin vände sig mot honom. Det var en snabb blick, men Jonas hann se den. Inte irritation. Inte heller samtycke. Mer en påminnelse.

Erik stannade upp.

“Eller”, sa han, långsammare, “vi behöver bestämma tillsammans vilka spår som faktiskt behövs.”

Karin log nästan omärkligt.

Jonas såg på Annika. Hon såg också. Det fanns ett språk mellan människor i förändring, tänkte han, som inte stod i någon modell. En sekunds paus kunde vara mer värd än en hel utbildning.

“Tre spår låter rimligt”, sa Annika. “Men driftbarhetsspåret måste börja med kriterier, inte önskningar.”

“Vad menar du?” frågade Nora.

Annika öppnade sin anteckningsbok. “Vad måste vara sant innan vi ens överväger produktion? Exempelvis: vad händer om meddelandetjänsten inte svarar, hur loggar vi, vem får larm, vad ser handläggaren, hur rullar vi tillbaka, vem äger incidenten?”

“Det där låter som en definition of done”, sa Fanny.

Jonas tittade på henne.

“Förlåt”, sa hon. “Jag vet att man inte ska kasta engelska ord på drift före lunch.”

“Det går bra om orden betyder något.”

Erik skrev inte på tavlan direkt. Han såg på Karin först.

“Vill du?” frågade han.

Det var en liten fråga, men rummet märkte den. Karin också. Hon reste sig och gick fram till whiteboarden. Tog pennan. För ett ögonblick såg hon inte ut som någon som försökte fylla en roll. Hon såg ut som någon som tog den.

Hon skrev:

**Vad visar vi?**  
**Vad lär vi oss?**  
**Vad är inte klart?**  
**Vad krävs för driftbarhet?**

Sedan vände hon sig mot gruppen.

“Jag vill att vi är brutalt ärliga på ledningsavstämningen”, sa hon. “Vi visar ett steg framåt, men vi säger också vad som inte är klart. Inte som ursäkt. Som ansvar.”

Erik nickade. “Det kommer väcka frågor.”

“Ja.”

“Birgitta kommer vilja veta varför vi inte har fångat det här tidigare.”

Karin höll kvar pennan i handen. “Då säger vi sanningen.”

“Vilken del?”

“Att vi fortfarande håller på att lära oss vad tidig involvering betyder. Och att drift inte var med tillräckligt tidigt, trots att vi sa att de skulle vara det.”

Jonas kände hur det drog till i honom. Inte för att meningen var dramatisk, utan för att den var ovanlig. Han var van att driftproblem beskrevs som tekniska upptäckter, resursbrister eller beroenden. Mer sällan som ett resultat av att någon inte hade skapat rätt samtal i tid.

“Det kommer inte låta så snyggt”, sa Erik.

“Nej”, sa Karin. “Men det kanske låter sant.”

Annika lutade sig tillbaka. “Jag kan leva med sant.”

Fanny höjde handen halvt. “Jag också, men får jag be om att sant inte blir en timmes självpiskning? Jag behöver faktiskt bygga om demovyn.”

“Noterat”, sa Karin.

De arbetade i fyrtiofem minuter. Det var ett rörigt arbete, men rörigheten hade riktning. Jonas gick igenom driftbarhetsriskerna. Annika formulerade kriterier som människor faktiskt kunde förstå. Fanny översatte dem till tekniska uppgifter utan att få dem att låta mindre viktiga. Nora skrev om demo-scenarierna så att handläggarnas behov stod i centrum. Erik höll ihop beroenden men avbröt sig själv varje gång han var på väg att säga “jag tar fram en plan” och frågade i stället vem som behövde vara med. Karin prioriterade bort två saker som tidigare låtit lockande men nu mest skulle ha skapat teater.

Det gjorde ont att se henne göra det.

Inte för att hon tvekade. För att hon inte tvekade tillräckligt för att kunna gömma sig bakom osäkerhet.

“Vi tar inte med automatisk formulering av nästa steg i den här demon”, sa hon.

Nora såg upp. “Men handläggarna har efterfrågat det.”

“Jag vet.”

“Det var ett av de tydligaste behoven.”

“Jag vet.”

Karin lade ner pennan och mötte Noras blick. “Men om vi tar med det nu kommer vi diskutera formuleringar och juridisk precision innan vi ens vet om statusstödet hjälper. Vi behöver lära i rätt ordning.”

Nora såg besviken ut. Inte arg, men besviken. Jonas såg hur Karin tog emot det. Där var produktägarens nej igen. Inte det stora, heroiska nej:et inför en styrgrupp, utan det lilla som sved i ett rum där alla försökte väl.

“Valt bort är inte glömt”, sa Erik lågt.

Karin vände blicken mot honom, och något passerade mellan dem. Tacksamhet, kanske. Eller en varning om att inte rädda henne för mycket.

“Precis”, sa hon. “Vi lägger det synligt som senare behov, med skälet till varför.”

Nora nickade, långsamt. “Okej. Då vill jag skriva skälet så handläggarna förstår att vi inte ignorerar dem.”

“Bra”, sa Karin. “Gör det.”

När mötet var slut stannade Jonas och Annika kvar medan de andra samlade ihop sig. Fanny försvann först, med datorn redan öppen i händerna. Nora gick efter henne, fortfarande skrivande. Erik blev kvar vid tavlan med Karin.

Jonas hörde inte allt de sa, men tillräckligt.

“Du gjorde det där bra”, sa Erik.

Karin stoppade ner pennan i sin väska. “Jag valde bort något som Nora hade jobbat fram.”

“Ja.”

“Det känns inte bra.”

“Nej.”

“Du är dålig på tröst.”

“Jag försöker att inte göra om obehag till framgångsspråk.”

Hon såg på honom. Sedan skrattade hon, tystare än vanligt. “Det uppskattar jag, tror jag.”

Erik log. Inte stort. Jonas tittade bort, av både artighet och självbevarelsedrift. Han hade ingen lust att bli vittne till början på något som senare kunde skapa ytterligare möten.

Annika däremot såg allt. Det gjorde hon alltid.

När Karin och Erik gick ut stannade hon vid Jonas sida och såg på whiteboarden.

“Det här var bättre”, sa hon.

“Det var fortfarande sent.”

“Ja.”

“Vi var fortfarande inte med från början.”

“Nej.”

Han väntade på att hon skulle säga något försonande. Det gjorde hon inte. Det var en av anledningarna till att han stod ut med henne.

“I nästa flöde ska vi vara med innan någon säger bara”, sa hon.

“Det borde vara en regel.”

“Då skriver vi den.”

Hon gick fram till tavlan och lade till längst ner:

**Ingen säger “bara” utan att drift får fråga vad det betyder.**

Jonas läste meningen och kände något som inte riktigt var optimism. Snarare en liten minskning av trötthet.

Det fick duga.

Senare samma eftermiddag kom ett nytt mejl från Erik till gruppen. Jonas öppnade det med den misstänksamhet han reserverade för allt som hade fler än tre mottagare.

Ämnesraden löd:

**Kompletteringsstöd: demo som lärande, inte låtsasleverans**

Jonas läste.

Mejlet var kortare än han väntat sig. Det sammanfattade vad de skulle visa, vad de inte skulle visa, vilka driftbarhetskriterier som behövde uppfyllas senare och hur de skulle kommunicera detta på ledningsavstämningen. Längst ner stod:

*Vi upptäckte detta tack vare att drift kom in. Nästa gång ska drift vara med tidigare, inte som sen kvalitetssäkring utan som del av utformningen.*

Jonas läste meningen två gånger.

Sedan skickade han den vidare till Annika med kommentaren:

*Han lär sig.*

Svaret kom efter några sekunder.

*De kanske gör det allihop.*

Jonas lutade sig tillbaka. Genom väggen hördes ett avlägset skratt från korridoren, sedan ljudet av någon som svor åt kaffemaskinen.

Myndigheten var fortfarande myndigheten.

Men för första gången på länge hade ett problem från drift inte bara blivit en sen invändning. Det hade blivit en fråga om hur de arbetade.

Det var inte klart.

Men det var inte ingenting.

---

Kort kapitelnotering:
- Viktiga händelser:
  - Jonas och Annika upptäcker att kompletteringsstödet är mer sårbart än gruppen förstått.
  - Drift visar att lösningen saknar tydlig fallback, rimliga timeouts, användbart felmeddelande, loggning och övervakning.
  - Gruppen tvingas skilja mellan demo för lärande och verklig produktionsklarhet.
  - Karin väljer bort automatisk formulering av nästa steg i demon för att fokusera lärandet.
  - Erik hejdar sin impuls att skapa en färdig plan och bjuder in gruppen att forma spåren tillsammans.
  - Driftbarhetskriterier formuleras som en nödvändig del av fortsatt arbete.
- Nya kontinuitetspunkter:
  - Rummet Utsikten saknar fönster och används för driftmötet.
  - Driftens vägglapp säger: “Inget är klart förrän det går att drifta.”
  - Regeln “Ingen säger ‘bara’ utan att drift får fråga vad det betyder” etableras.
  - Demot ska visa stödlogik och handläggarbehov, inte låtsas vara produktionsklart.
  - Kompletteringsstödet behöver fallback, timeouts, felmeddelande, loggning och övervakning före produktion.
- Relationsförändringar:
  - Jonas och Annika får tydligare respekt från Karin och Erik.
  - Karin visar produktägarmognad genom att välja bort ett efterfrågat behov.
  - Erik stödjer Karin utan att ta över, men hans planeringsimpuls finns kvar.
  - Fanny, Nora och drift börjar hitta ett mer praktiskt samarbete.
- Öppna frågor:
  - Hur reagerar ledningen när piloten visar lärande i stället för nästan färdig leverans?
  - Kommer drift involveras tidigare nästa gång eller faller gruppen tillbaka?
  - Hur hanterar Karin besvikelsen hos handläggare när efterfrågade funktioner väljs bort?
