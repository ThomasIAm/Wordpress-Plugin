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

## Update ##

Updaten je Wordpress en je plugins. Als er plugins zijn die lang niet zijn geüpdate dan is het misschien goed om te kijken naar een alternatieve plugin die wel regelmatig wordt geüpdate en veel actieve gebruikers heeft.

## HTTPS Prefix ##

Gebruik een HTTPS prefix. Zorg ervoor dat er geen data (en al helemaal geen gevoelige data) over HTTP wordt verzonden. HTTP verstuurd gegevens zonder ze te encrypten. HTTPS verstuurd de gegevens nadat ze zijn versleuteld. Dit maakt het voor de aanvallers veel lastiger om bij de daadwerkelijke gegevens te komen.

## MFA ##

Één van de belangrijkste stappen voor je veiligheid is het aanzetten van Multi-Factor-Autenticatie! Dit maakt het voor de aanvaller veel moeilijker om ergens in te loggen.

Stel de aanvaller heeft de gebruikersnaam en wachtwoord, dan zal hij nog een (aantal) stappen moeten ondergaan om in te loggen. Dit kan bijvoorbeeld door een authenticator app op je mobiel.

## Verberg WP-login ##

Het verbergen van je wp-login scherm is een handige tip zodat er niet de standaard admin login pagina wordt gebruikt. Je kan hiervoor bijvoorbeeld `WPS Hide Login` gebruiken. Hiermee kun je de url van je admin inlog pagina aanpassen. Zorg dat je deze url ergens veilig bewaard.

