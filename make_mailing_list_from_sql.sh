#!/bin/sh

mysql -p --skip-column-names -e \
"SELECT CONCAT_WS('|', formal_title,
name_first, name_last, email_address)
AS 'Contact Information for Premium Members'
FROM the_db.member_info WHERE membership_type = 'premium'
AND membership_expiration > CURDATE();" > contact_list.txt
