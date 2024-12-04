FROM ameseraph/su_group_29:latest

COPY init.sh /passoire/init.sh
COPY crypto-helper.sh /passoire/crypto-helper/crypto-helper.sh
COPY ./web/connexion.php /passoire/web/connexion.php
COPY ./web/file_upload.php /passoire/web/file_upload.php
COPY ./web/index.php /passoire/web/index.php
COPY ./web/signup.php /passoire/web/signup.php
COPY download.php /passoire/web/download.php
COPY ./crypto-helper/server.js /crypto-helper/server.js
