# Installatie phpMyAdmin

phpMyAdmin is een hulpmiddel om de database van WordPress te beheren. Nadat WordPress is geinstalleerd kan phpMyAdmin worden geinstalleerd; voer hiervoor het volgende kommando uit:

    sudo apt install phpmyadmin

En afhankelijk van de onderliggende webserver technologie de volgende kommando's:

Voor een Apache server:

    sudo ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-available/phpmyadmin.conf
    sudo a2enconf phpmyadmin.conf
    sudo service apache2 reload

Voor een Nginx server:

    sudo ln -s /user/share/phpmyadmin /var/www/public_html/phpmyadmin
    nginx -s reload

phpMyAdmin draait als web applicatie en wordt gestart in een browser met de volgende URL:

    localhost/phpmyadmin/

Er kan nu worden ingelogd met de gebruiker en wachtwoord zoals opgegeven tijdens de installatie van WordPress. Hierna kan de database behorend bij WordPress worden bekeken en beheerd.

# Installatie www.bad-neighborhood.com Website Simulator

De ontwikkelaar van de Login LockDown plugin heeft een eigen website www.bad-neighborhood.com en om daar geen gebruik van te hoeven maken wordt er gebruik gemaakt van een simulatie die lokaal op de machine draait.

Voer de volgende stappen uit om deze lokaal te installeren.

Maak een subfolder in de Applications subfolder:

    ~$ cd ~/Applications
    ~/Applications$ mkdir www.bad-neighborhood.com

Pak de zip file uit in de net aangemaakte subfolder. Hierna staan in deze folder in ieder geval twee bestanden:

    index.html
    server.py

Start de simulator met:

    ./server.py

Indien succesvol gestart verschijnt de logging:

    INFO:root:Starting httpd...

De website simulator draait op poort 10000 en dus kan de home page van de website worden bezocht in een browser met de volgende URL:

    localhost:10000

# Installatie Laatste Versie van de Login LockDown plugin

In een van de stappen hiervoor is versie 1.8.1 van de Login LockDown plugin geinstalleerd. Op de website simulator is een nieuwste versie 1.8.2 beschikbaar die geinstalleerd moet worden. Ergens op de pagina staat een link:

    Download: Login LockDown v1.8.2

Klik op deze link en hierna wordt de zip file login-lockdown.1.8.2.zip gedownload en geplaatst in de Downloads folder.

Volg nu dezelfde instructies waarmee versie 1.8.1 werd geinstalleerd, echter nu wordt deze overschreven door deze laatste versie 1.8.2.

1. Kontroleer op de WordPress admin pagina of nu inderdaad versie 1.8.2 actief is.
2. Probeer nu weer eens in te loggen met een onjuist wachtwoord.
3. Log nu weer in met het juiste wachtwoord.
4. Kontroleer in phpMyAdmin of er inderdaad weer een logging wordt vermeld van het gebruik van een verkeerd wachtwoord.

Ga nu terug naar de www.bad-neighborhood.com website simulator in de browser.

Onderaan de pagina staat:

    Read our disclaimer & secrets

Klik op de secrets link en wees verbaasd over wat er nu getoond wordt op het scherm!