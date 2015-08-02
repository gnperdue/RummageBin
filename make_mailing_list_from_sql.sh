#!/bin/sh

mysql -p --skip-column-names -e \
"SELECT CONCAT_WS(',',
IFNULL(formal_title, ' '),
IFNULL(name_first, ' '),
IFNULL(name_last, ' '),
IFNULL(email_address, ' '))
FROM the_db.member_info WHERE membership_type = 'premium'
AND membership_expiration > CURDATE();" > contact_info.txt
