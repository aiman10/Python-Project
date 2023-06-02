Het project is verdeeld over 10 bestanden, waarbij elk bestand slechts één deel van de applicatie regelt. Het bestand appmodule.py exporteert een superklasse die modules moeten erven. De basismodule heeft twee methoden die kunnen worden overschreven, een run methode die kan worden aangeroepen om de code van de module uit te voeren en een get_output methode die de uitvoer van de run methode retourneert.

4 modules breiden de superklasse uit:
FileModule die alle bestanden in de C-schijf probeert op te halen.
PingModule die een bepaalde url 1000 keer achter elkaar pingt, deze module kan gebruikt worden als DDOS service.
ScreenModule die een screenshot maakt van het scherm van de gebruiker en de inhoud codeert als base64.
SysInfoModule die de systeeminformatie van de gebruiker ophaalt.

Deze modules kunnen worden geladen met de klasse Loader. De klasse Loader biedt een statische methode die een module uit een bestand laadt en terugstuurt naar de aanroeper.

Het startpunt van de applicatie is in main.py, main.py biedt meerdere functies om de programmastroom te regelen.

Het eerste wat main.py probeert, is het installeren van afhankelijkheden die andere modules nodig hebben. Als dat lukt, importeren we deze afhankelijkheden, daarna maken we een verbinding met de github repo en halen daar de coderingssleutel vandaan.
Vervolgens controleren we of de gebruiker een willekeurig gegenereerd id-bestand op zijn apparaat heeft, als dat gevonden wordt lezen we zijn id uit en anders genereren we een nieuwe, dit helpt bij het identificeren van de gebruikers en de kans op botsingen is zeer minimaal.

Nadat alles is ingesteld, voeren we sysinfomodule uit en sturen we de uitvoer terug naar de github repo.
Dan gaan we naar de hoofdprogrammalus waar we elke 30 minuten een "actie"-bestand proberen op te halen van de repo. Het actiebestand mag niet versleuteld zijn, maar het moet een naam van een module zijn die base64 gecodeerd is.

Vervolgens halen we de module op van de github repo, de module zou versleuteld en base64 gecodeerd moeten zijn.
We decoderen en ontsleutelen de module en posten de uitvoer indien nodig terug naar de repo.

**Features:**

* Dynamisch laden van modules: Het gebruik van de klasse Loader maakt het dynamisch laden van modules mogelijk op basis van hun bestandsnamen. Dit zorgt voor flexibiliteit en uitbreidbaarheid, omdat nieuwe modules kunnen worden toegevoegd zonder de kerncode van de applicatie aan te passen.
* Versleutelde communicatie: De applicatie versleutelt gevoelige data voordat het naar de GitHub repository wordt verzonden, en zorgt zo voor veilige communicatie tussen de geïnfecteerde hosts en de hackers. Versleuteling wordt uitgevoerd met behulp van de cryptografie bibliotheek.
* GitHub Integratie: De applicatie maakt gebruik van de PyGitHub bibliotheek om te communiceren met een GitHub repository. Het haalt versleutelde modules op, haalt configuratiebestanden op en logt verkregen gegevens naar de repository.

**Gemaakte keuzes:**

* Modulair ontwerp: De beslissing om de applicatie te structureren met behulp van klassen en objecten bevordert de duidelijkheid, onderhoudbaarheid en herbruikbaarheid van componenten. Elke module breidt de superklasse BaseModule uit en biedt zo een consistente interface voor het uitvoeren en ophalen van uitvoer.
* GitHub als communicatiekanaal: Het gebruik van GitHub als communicatiekanaal biedt een gecentraliseerd en toegankelijk platform voor configuratie en gegevensuitwisseling. Het maakt eenvoudig beheer op afstand en controle van geïnfecteerde hosts mogelijk.

**Moeilijkheden:**

* Het was een uitdaging zijn om ervoor te zorgen dat de applicatie naadloos werkt op verschillende besturingssystemen, Python-versies en afhankelijkheden. Grondig testen en compatibiliteitscontroles zijn nodig om deze problemen te beperken.
* Beveiligingsrisico's: Het bouwen van een veilige Trojan agent of agent framework brengt inherente risico's met zich mee. Het implementeren van robuuste encryptie, het veilig beheren van authenticatietokens en het beperken van de kans op misbruik of ongeautoriseerde toegang vereisen zorgvuldige overweging.

**Onopgeloste problemen:**

* Foutafhandeling en uitzonderingsbeheer: Het implementeren van uitgebreide mechanismen voor foutafhandeling kan de robuustheid en veerkracht van de applicatie verbeteren.
* Uitbreidbaarheid en schaalbaarheid: Hoewel de applicatie momenteel een set voorgedefinieerde modules ondersteunt, kan toekomstige uitbreiding en de mogelijkheid om eenvoudig aangepaste modules toe te voegen een gebied zijn dat verdere aandacht vereist.
