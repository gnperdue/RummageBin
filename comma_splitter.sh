#!/bin/bash

ENERGYSTRING="1,9"
ARR=$(echo $ENERGYSTRING | tr "," "\n")
for x in $ARR
do
  echo $x
done

echo ${ARR[0]}
echo ${ARR[1]}

