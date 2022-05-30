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

`sudo apt update
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
                 php-zip`

 ## installeer Wordpress ##

 Om Wordpress te installeren gebruiken we de volgende commando's:

 `sudo mkdir -p /srv/www
sudo chown www-data: /srv/www
curl https://wordpress.org/latest.tar.gz | sudo -u www-data tar zx -C /srv/www`

