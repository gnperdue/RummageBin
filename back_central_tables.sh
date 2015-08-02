#!/bin/sh

mysqldump --user='root' -p --skip-lock-tables \
  information_schema > bck_information_schema.sql
mysqldump --user='root' -p --skip-lock-tables \
  mysql > bck_mysql.sql
mysqldump --user='root' -p --skip-lock-tables \
  performance_schema > bck_performance_schema.sql
