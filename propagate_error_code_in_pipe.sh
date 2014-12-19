#!/bin/bash
if [ -d lamp ]; then
  rm -rf lamp
fi
git clone https://github.com/GENIEMC/lamp.git
pushd lamp
###git checkout -b R-2_8_6.4-br R-2_8_6.4
OUT=$( ./rub_the_lamp.sh -s -p 6 --support-tag HEAD | tee lamp_log.txt ; exit ${PIPESTATUS[0]} );
if [[ $? == 0 ]]; then
  echo "Success"
else
  cat lamp_log.txt
  exit 1
fi
popd
