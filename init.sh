#!/bin/bash

#Nothing to see here
if [[ -d /passoire/flags-enc ]]; then
	/passoire/.h/b.sh
	/passoire/flags/init.sh
fi



# Start DB, web server and ssh server
service mysql start
service ssh start
service apache2 start


DB_NAME="passoire"
DB_USER="passoire"
DB_PASSWORD=$(head -n 1 /passoire/config/db_pw)
# Adapt to our ip
echo "127.0.0.1 db" >> /etc/hosts

	
if ls /passoire/logs/initialized >/dev/null 2>&1; then
	echo "Initialization has already been performed"
else
# Initialize database
	echo "Creating MySQL database and user..."
	mysql -u root -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};"
	mysql -u root -e "CREATE USER IF NOT EXISTS '${DB_USER}'@'localhost' IDENTIFIED BY '${DB_PASSWORD}';"
	#mysql -u root -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'localhost';"
	mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO '${DB_USER}'@'localhost' WITH GRANT OPTION;"
	mysql -u root -e "FLUSH PRIVILEGES;"

	mysql -u root ${DB_NAME} < config/passoire.sql

	# Redirect querry from website root to our main page
	rm /var/www/html/index.html
	echo "<?php header(\"Location: passoire/index.php\"); ?>" > /var/www/html/index.php

	# Link apache dir and our web dir
	ln -s /usr/share/phpmyadmin/ /var/www/html/phpmyadmin
	ln -s /passoire/web/ /var/www/html/passoire
	
	touch /passoire/logs/initialized
fi
	
	
if [ -z "${HOST+x}" ] || [ -z "${HOST}" ]; then
	HOST=$(hostname -i)
fi

echo "Web server running at http://$HOST"

# Adapt to HOST variable regardless of past modifications.
sed -E -i "s/^const host = \"(CONTAINER_IP|localhost|[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\";$/const host = \"$HOST\";/" /passoire/crypto-helper/server.js
sed -E -i "s@http://(CONTAINER_IP|localhost|[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):3002@http://$HOST:3002@g" /passoire/web/crypto.php

# Fix bug with DES encryption/decryption
sed -i 's/ -provider legacy -provider default//g' /passoire/crypto-helper/server.js


touch /passoire/logs/crypto-helper.log

# Start crypto helper api
/passoire/crypto-helper/crypto-helper.sh start

# Monitor logs
tail -f /passoire/logs/crypto-helper.log /var/log/apache2/access.log /var/log/apache2/error.log
