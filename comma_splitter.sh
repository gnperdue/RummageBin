#!/bin/bash

ENERGYSTRING="1,9"
echo "The raw string is $ENERGYSTRING"

# replace commas with spaces, wrap in an array
ARR=($(echo $ENERGYSTRING | tr "," " "))

# get length
ARRLEN=${#ARR[@]}
echo "The split array length is $ARRLEN"

if [[ $ARRLEN -gt 1 ]]; then
  echo "The array length is greater than 1"
fi

echo "For loop:"
for x in ${!ARR[@]}
do
  echo "  Index $x = ${ARR[x]}"
done

echo "Direct access also: "
echo "  Index 0 = ${ARR[0]}"
echo "  Index 1 = ${ARR[1]}"

