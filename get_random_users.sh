#!/usr/bin/env bash

JQ=`which jq`
if [[ $JQ == "" ]]; then
  echo "You must have jq installed to use this script."
  exit 1
fi
CSVLOOK=`which csvlook`
if [[ $CSVLOOK == "" ]]; then
  echo "You must have csvlook installed to use this script."
  exit 1
fi
CSVSQL=`which csvsql`
if [[ $CSVSQL == "" ]]; then
  echo "You must have csvsql installed to use this script."
  exit 1
fi

FILEBASE="rusers"
CHATTY="false"
NUSERS=10

# Get a set of random users
curl -s "http://api.randomuser.me/?results=${NUSERS}" > ${FILEBASE}.json

# Look at what we got
if [[ $CHATTY == "true" ]]; then
  jq "." ${FILEBASE}.json
fi

# Just get a few fields 
< ${FILEBASE}.json jq -r "[.results[] | {first: .user.name.first, last: .user.name.last, sex: .user.gender, email: .user.email, street: .user.location.street, city: .user.location.city, state: .user.location.state, zipcode: .user.location.zip}]" > ${FILEBASE}_filtered.json

# Turn the JSON to flat csv
< ${FILEBASE}_filtered.json json2csv -f first,last,sex,email,street,city,state,zipcode > ${FILEBASE}_filtered.csv

# Look at what we got
if [[ $CHATTY == "true" ]]; then
  < ${FILEBASE}_filtered.csv csvlook
fi

# Merge some columns with csvsql
< ${FILEBASE}_filtered.csv csvsql \
  --query "SELECT first || ' ' || last AS name, sex, email, street, city, state, zipcode FROM stdin" \
  > ${FILEBASE}_filtered_merged.csv

# Look at what we got
if [[ $CHATTY == "true" ]]; then
  csvlook ${FILEBASE}_filtered_merged.csv
fi

# Make a head file and a body file
head -n 1 ${FILEBASE}_filtered_merged.csv > ${FILEBASE}_filtered_merged_header.csv
cat ${FILEBASE}_filtered_merged.csv | header -d -n 1 > ${FILEBASE}_filtered_merged_body.csv
