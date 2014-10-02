#!/bin/bash

#
# For the 2.8.X patch series, we must point LHAPATH into an area in $GENIE
# 
TAG=$1  # R-2_8_4, etc.
ENVFILE=$2
GENIEDIRNAME=$3
MAJOR=`echo $TAG | cut -c3-3`
MINOR=`echo $TAG | cut -c5-5`
PATCH=`echo $TAG | cut -c7-7`
echo "$MAJOR $MINOR $PATCH"

if [[ $MAJOR == 2 ]]; then
  if [[ $MINOR == 8 ]]; then
    if [[ $PATCH > 0 ]]; then
      perl -ni -e 'print if !/LHAPATH/' $ENVFILE  # remove just the LHAPATH line
      echo "export LHAPATH=`pwd`/$GENIEDIRNAME/data/evgen/pdfs" >> $ENVFILE
    fi
  fi
fi

