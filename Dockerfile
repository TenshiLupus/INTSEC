FROM ameseraph/su_group_29:latest

# COPY init.sh /passoire/init.sh
# COPY crypto-helper.sh /passoire/crypto-helper/crypto-helper.sh

COPY ./web/connexion.php /passoire/web/connexion.php
COPY ./web/file_upload.php /passoire/web/file_upload.php
COPY ./web/index.php /passoire/web/index.php
COPY ./web/signup.php /passoire/web/signup.php
COPY ./web/db_connect.php /passoire/web/db_connect.php
COPY ./web/message_board.php /passoire/web/message_board.php
COPY ./web/my_files.php /passoire/web/my_files.php
COPY ./crypto-helper/server.js /passoire/crypto-helper/server.js
COPY download.php /passoire/web/download.php
