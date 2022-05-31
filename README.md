# README #

Dit is een README voor het installeren van Wordpress op een Ubuntu OS.

Deze README gaat niet in hoe Ubuntu te installeren. Het is raadzaam om de OS te installeren op een VM (Virtual Machine).

## Inhoudsopgave ##

* installeer dependencies
* installeer Wordpress
* configureer Apache
* configureer database
* configureer Wordpress met database
* configureer Wordpress

## installeer dependencies ##

Om Apache en PHP te installeren gebruiken we de volgende commando's in de terminal:

`sudo apt update`

    sudo apt install apache2 \
                 ghostscript \
                 libapache2-mod-php \
                 mysql-server \
                 php \
                 php-bcmath \
                 php-curl \
                 php-imagick \
                 php-intl \
                 php-json \
                 php-mbstring \
                 php-mysql \
                 php-xml \
                 php-zip

 ## installeer Wordpress ##

 Om Wordpress te installeren gebruiken we de volgende commando's:

`sudo mkdir -p /srv/www`

`sudo chown www-data: /srv/www`

`curl https://wordpress.org/latest.tar.gz | sudo -u www-data tar zx -C /srv/www`

## Apache ##

Maak een Apache site aan. Maak een folder in 
`/etc/apache2/sites-available/wordpress.conf`.

Zet daarin de volgende code:

    <VirtualHost *:80>

        DocumentRoot /srv/www/wordpress

        <Directory /srv/www/wordpress>

            Options FollowSymLinks

            AllowOverride Limit Options FileInfo

            DirectoryIndex index.php

            Require all granted

        </Directory>

        <Directory /srv/www/wordpress/wp-content>

            Options FollowSymLinks

            Require all granted

        </Directory>

    </VirtualHost>

Daarna moet de site 'aangezet' worden met het volgende commando:

`sudo a2ensite wordpress`


Toestaan van URL herschrijven:

`sudo a2enmod rewrite`


Zet de default "It Works" site uit:

`sudo a2dissite 000-default`


Start daarna de Apache service opnieuw op:

`sudo service apache2 reload`
## Database ##

We maken een MySQL database met de volgende commando's:

Stap 1

`sudo mysql -u root`

Stap 2 (dit zijn de commando's in mysql)

`CREATE DATABASE wordpress;`

`CREATE USER wordpress@localhost IDENTIFIED BY 'voeg hier je wachtwoord in';`

    GRANT SELECT, INSERT,UPDATE,DELETE,CREATE,DROP,ALTER
        -> ON wordpress.*
        -> TO wordpress@localhost;

`FLUSH PRIVILEGES;`

`quit`


Daarna start je de mysql service:

`sudo service mysql start`
## Wordpress met database ##

In deze stap gaan we Wordpress met de database koppelen.

Allereerst kopieer het 'sample' bestand naar `wp-config-php`.

Dit doen we door het volgende commando te gebruiken:

`sudo -u www-data cp /srv/www/wordpress/wp-config-sample.php /srv/www/wordpress/wp-config.php`

In de volgende stap worden de credentials aangemaakt. <bold>Let op</bold> verander de volgende gedeeltes niet in het commando `database_name_here` en `username_here`.

Je vervangt wel `your password` met je database wachtwoord!

    sudo -u www-data sed -i 's/database_name_here/wordpress/' /srv/www/wordpress/wp-config.php
    sudo -u www-data sed -i 's/username_here/wordpress/' /srv/www/wordpress/wp-config.php
    sudo -u www-data sed -i 's/password_here/<your-password>/' /srv/www/wordpress/wp-config.php

Open daarna de configuration file in nano (of welke tekst-editor je gebruikt):

`sudo -u www-data nano /srv/www/wordpress/wp-config.php`

Zoek naar de volgende tekst:

    define( 'AUTH_KEY',         'put your unique phrase here' );
    define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
    define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
    define( 'NONCE_KEY',        'put your unique phrase here' );
    define( 'AUTH_SALT',        'put your unique phrase here' );
    define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
    define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
    define( 'NONCE_SALT',       'put your unique phrase here' );

Verwijder deze tekst.

En vervang het met onderstaande tekst:

    define('AUTH_KEY',         'H@6-|$v-I]pkBDUTrP)zN7;.t]n%,!@OLrt0jLx/u >|a<#NuwPM02FT  UF3]-E');
    define('SECURE_AUTH_KEY',  'F1*I_O;KYuQ[N|R_Xy*h^0>s3%ddO6u%-;p[+-p2j(}?sE8iB&gw8UNpYqLI0cpy');
    define('LOGGED_IN_KEY',    '~_-l$g)|#&zlEu+;^7G0-.K)wu/p0%4=Nb;WJ4H`<YVdF{LSO^#t$H&#eB=|st#&');
    define('NONCE_KEY',        ']X?Mk6+743-@:n{rl%RJqp|^S1r2*>|2fo?=D5a=F+wR^k>Tf|vyZ `8a>&u-O!(');
    define('AUTH_SALT',        '/c=g1idW6 ]L>hO,B4nL]QLfyVt+O,V.FY,-iFzkp</h4I9!Yx&c!>RYH^5uIV2v');
    define('SECURE_AUTH_SALT', 'lD4i?nW@o`!e@OP3vn^5VVyOI5c%fa`t-bEJ;T-F+j#:nV&(mV9J|n5XjdK>h0a~');
    define('LOGGED_IN_SALT',   'r{J#m]/_zN2],Wy+{^HnA9R|1pC8dM9JF{>>a F~Tttgr;*(,yE&T9;oK`@i?f^3');
    define('NONCE_SALT',       'S{-L5WN/^cW9VT1VEkZah$885$%T>N)v~q=)3LebN1B,rlK<u]6Lq9.`w9$l60jh');

Dit is de <a href="https://api.wordpress.org/secret-key/1.1/salt/">link</a> naar bovenstaande tekst.

Sla het bestand op.
## Wordpress configuratie ##

Open nu een browser en ga naar <a href="http://localhost/">http://localhost/</a>.

Volg hier het installatie proces. 

Daarna kun je inloggen via <a href="http://localhost/wp-login.php">http://localhost/wp-login.php</a>
<br>
<br>
<br>
Je Wordpress website is klaar om te gebruiken!

Ga nu verder om phpmyadmin te configureren.

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