#!/usr/bin/env bash

TAG=R-2_8_6
MAJOR=`echo $TAG | cut -c3-3`
MINOR=`echo $TAG | cut -c5-5`
PATCH=`echo $TAG | cut -c7-7`


if [[ $MAJOR == 2 ]]; then
  if [[ $MINOR == 8 ]]; then
    if [[ $PATCH -ge 2 && $PATCH -le 4 ]]; then
      echo "DO THE THING!"
    else
      echo "Do not do the thing..."
    fi 
  fi
fi

GENIEVER=GENIE_2_8
MAJOR=`echo $GENIEVER | cut -c7-7`
MINOR=`echo $GENIEVER | cut -c9-9`
PATCH=`echo $GENIEVER | cut -c11-11`
if [[ $PATCH == "" ]]; then
  PATCH=0
fi
echo "$MAJOR $MINOR $PATCH"

GENIEVER=GENIE_2_8_6
MAJOR=`echo $GENIEVER | cut -c7-7`
MINOR=`echo $GENIEVER | cut -c9-9`
PATCH=`echo $GENIEVER | cut -c11-11`
echo "$MAJOR $MINOR $PATCH"


