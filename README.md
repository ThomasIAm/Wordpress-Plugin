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
`sudo apt install apache2 \`
                 `ghostscript \`
                 `libapache2-mod-php \`
                 `mysql-server \`
                 `php \`
                 `php-bcmath \`
                 `php-curl \`
                 `php-imagick \`
                 `php-intl \`
                 `php-json \`
                 `php-mbstring \`
                 `php-mysql \`
                 `php-xml \`
                 `php-zip`

 ## installeer Wordpress ##

 Om Wordpress te installeren gebruiken we de volgende commando's:

`sudo mkdir -p /srv/www`
`sudo chown www-data: /srv/www`
`curl https://wordpress.org/latest.tar.gz | sudo -u www-data tar zx -C /srv/www`

## Apache ##

Maak een Apache site aan. Maak een folder in 
`/etc/apache2/sites-available/wordpress.conf`

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

## Wordpress met database ##

## Wordpress configuratie ##

