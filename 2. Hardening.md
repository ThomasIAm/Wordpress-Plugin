# Hardening Wordpress #

In deze readme gaan we kijken hoe we de Wordpress pagina kunnen harden tegenover attackers.

Er worden hieronder een aantal voorbeelden gegeven. Dit is geen volledige lijst omdat de zoveel items zijn dat deze readme onleesbaar wordt.
Daarom is er een referentie sectie toegevoegd waar een aantal voorbeelden worden gegeven van hardening guidelines. Ga vooral zelf ook op zoek naar goede bronnen. Daarnaast worden deze guidelines steeds geüpdated dus het is raadzaam eens in de zoveel tijd de guidelines er opnieuw bij te pakken en te controleren of ze nog van toepassing zijn.

100% veiligheid is een utopie. Het streven naar die 100% is iets om naar te streven. Alle maatregelen die je toepast zorgen voor extra veiligheid, maar aanvallers vinden altijd manieren om dit te omzeilen.
Het is dus van belang om het ze nu zo moeilijk mogelijk te maken. Daar is deze readme voor bedacht en geschreven.

## Inhoudsopgave ##

- [Downloading files](#downloading-files)
- [Check Code](#check-code)
- [Source Code Checker](#source-code-checker)
- [Update](#update)
- [HTTPS Prefix](#https-prefix)
- [MFA](#mfa)
- [Verberg WP-login](#verberg-wp-login)
- [Security Plugins](#security-plugins)
- [Referenties](#referenties)

## Downloading Files <a name="downloading-files"></a>

Het downloaden van een bestand is altijd een gevaarlijke actie om uit te voeren. De eerste vraag die je jezelf kan stellen "Waarom moet ik dit bestand downloaden?" de vraag stellen is veelal hem ook beantwoorden. Mocht je het bestand toch downloaden dan kun je deze door <a href="https://www.virustotal.com">Virustotal</a> halen om te kijken of er malware op zit die al bekend is bij een aantal grote security bedrijven. Dit is zeker niet fool-proof, maar geeft een extra laag aan defensie.

Je kunt op internet zoeken of er mensen zijn die eerdere ervaringen delen over de bestanden. 

## Check Code <a name="check-code"></a>

Je kunt de code van de plugin bekijken en doorlezen. Je kunt als je wat meer gevordert bent zoeken naar bepaalde functies die niet noodzakelijk en als onveilig worden beschouwd. Dit zijn functies zoals: eval en exec. Dit kan je doen door `ctrl + f` te gebruiken om te zoeken naar bepaalde woorden. Wederom is dit niet 100% betrouwbaar want er zijn mogelijkheden om dit te omzeilen, maar het helpt bij de defensie en om op te sporen of je plugin hebt die niet precies doet wat jij wil dat die doet.

## Source Code Checker <a name="source-code-checker"></a>

Het is altijd goed om je plugins te controleren en dit kun je doen door bijvoorbeeld een source code checker te gebruiken. Een aantal voorbeelden van tools zijn: Wpsploit en Plugin Inspector (Wordpress plugin).

Deze tools kijken naar functies en mogelijke aanvallen die kunnen worden gedaan op basis van die functies.

## Update <a name="update"></a>

Updaten je Wordpress en je plugins. Als er plugins zijn die lang niet zijn geüpdate dan is het misschien goed om te kijken naar een alternatieve plugin die wel regelmatig wordt geüpdate en veel actieve gebruikers heeft.

## HTTPS Prefix <a name="https-prefix"></a>

Gebruik een HTTPS prefix. Zorg ervoor dat er geen data (en al helemaal geen gevoelige data) over HTTP wordt verzonden. HTTP verstuurd gegevens zonder ze te encrypten. HTTPS verstuurd de gegevens nadat ze zijn versleuteld. Dit maakt het voor de aanvallers veel lastiger om bij de daadwerkelijke gegevens te komen.

## MFA <a name="mfa"></a>

Één van de belangrijkste stappen voor je veiligheid is het aanzetten van Multi-Factor-Autenticatie! Dit maakt het voor de aanvaller veel moeilijker om ergens in te loggen.

Stel de aanvaller heeft de gebruikersnaam en wachtwoord, dan zal hij nog een (aantal) stappen moeten ondergaan om in te loggen. Dit kan bijvoorbeeld door een authenticator app op je mobiel.

## Verberg WP-login <a name="verberg-wp-login"></a>

Het verbergen van je wp-login scherm is een handige tip zodat er niet de standaard admin login pagina wordt gebruikt. Je kan hiervoor bijvoorbeeld `WPS Hide Login` gebruiken. Hiermee kun je de url van je admin inlog pagina aanpassen. Zorg dat je deze url ergens veilig bewaard.

## Security Plugins <a name="security-plugins"></a>

Ondanks ons voorbeeld van onze eigen plugin die gebaseerd is op de Login Lockdown plugin, is dit wel een goede plugin om te gebruiken. Je kunt namelijk na een aantal verkeerde inlog pogingen de toegang blokkeren voor een bepaalde tijd. Er zijn nog een aantal settings die je kunt wijzigen.

Er zijn meerdere plugins die de security verhogen van je Wordpress, maar **let dus wel op dat je niet zomaar iets download en installeerd!** Gebruik de officiële kanalen dan is de kans het kleinst dat er iets mis gaat. Wees er op bedacht of de plugin veel wordt gebruikt of wordt geüpdate. **Blijf dus altijd kritisch!**

## Referenties <a name="referenties"></a>

Dit zijn een aantal referenties naar hardening guidelines die bijdragen aan de veiligheid van je Wordpress website.

- <a href="https://wordpress.org/support/article/hardening-wordpress/">Wordpress Hardening</a>
- <a href="https://secure.wphackedhelp.com/blog/wordpress-security-checklist-guide/">Wordpress Security Checklist</a>

Dit zijn een aantal guidelines om je Wordpress beter te beveiligen. Er zijn nog veel meer guidelines te vinden. Bekijk ze kritisch en pas ze toe als ze de beveiliging ten goede komen.