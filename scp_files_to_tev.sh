#!/bin/bash

START=0
STOP=0

if [[ $# == 1 ]]; then
  STOP=$1
elif [[ $# > 1 ]]; then
  START=$1
  STOP=$2
fi

for i in `seq ${START} 1 ${STOP}`
do
  paddednum=`echo $i | perl -ne 'printf "%04d",$_;'`
  filename=minosmatch_fuel_me1Amc_zseg${paddednum}.hdf5
  scp $filename perdue@tev.fnal.gov:/phihome/perdue/theano/data/
done
