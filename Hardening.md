# Hardening Wordpress #

In deze readme gaan we kijken hoe we de Wordpress pagina kunnen harden tegenover attackers.

## Inhoudsopgave ##

* 
* 
* 

## Downloading Files ##

Het downloaden van een bestand is altijd een gevaarlijke actie om uit te voeren. De eerste vraag die je jezelf kan stellen "Waarom moet ik dit bestand downloaden?" de vraag stellen is veelal hem ook beantwoorden. Mocht je het bestand toch downloaden dan kun je deze door <a href="https://www.virustotal.com">Virustotal</a> halen om te kijken of er malware op zit die al bekend is bij een aantal grote security bedrijven. Dit is zeker niet fool-proof, maar geeft een extra laag aan defensie.

Je kunt op internet zoeken of er mensen zijn die eerdere ervaringen delen over de bestanden. 

## Check Code ##

Je kunt de code van de plugin bekijken en doorlezen. Je kunt als je wat meer gevordert bent zoeken naar bepaalde functies die niet noodzakelijk en als onveilig worden beschouwd. Dit zijn functies zoals: eval en exec. Dit kan je doen door `ctrl + f` te gebruiken om te zoeken naar bepaalde woorden. Wederom is dit niet 100% betrouwbaar want er zijn mogelijkheden om dit te omzeilen, maar het helpt bij de defensie en om op te sporen of je plugin hebt die niet precies doet wat jij wil dat die doet.

## Source Code Checker ##

Het is altijd goed om je plugins te controleren en dit kun je doen door bijvoorbeeld een source code checker te gebruiken. Een aantal voorbeelden van tools zijn: Wpsploit en Plugin Inspector (Wordpress plugin).

Deze tools kijken naar functies en mogelijke aanvallen die kunnen worden gedaan op basis van die functies.