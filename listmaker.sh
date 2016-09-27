#!/bin/bash

ROOTD=/lustre/atlas/proj-shared/hep105/sohini/vertex/snapshots

LE_FROOT="50_LE_DANN_2016-09-20T16.08.00.098418_iter_"
data_FROOT="50_dataDANN_2016-09-13T21.21.48.709808_iter_"
no_FROOT="50_noDANN_2016-09-10T10.05.03.739066_iter_"

ls $ROOTD/$LE_FROOT* > le_raw.txt
ls $ROOTD/$data_FROOT* > data_raw.txt
ls $ROOTD/$no_FROOT* > no_raw.txt

if [[ -f le_numbers.txt ]]; then
  rm le_numbers.txt
fi
touch le_numbers.txt
for filen in `ls $ROOTD/$LE_FROOT*solverstate`
do
  echo $filen | perl -ne '@l=split("_",$_);@m=split("\\.",@l[5]);print @m[0]."\n"' >> le_numbers.txt
done

if [[ -f data_numbers.txt ]]; then
  rm data_numbers.txt
fi
touch data_numbers.txt
for filen in `ls $ROOTD/$data_FROOT*solverstate`
do
  echo $filen | perl -ne '@l=split("_",$_);@m=split("\\.",@l[4]);print @m[0]."\n"' >> data_numbers.txt
done

if [[ -f no_numbers.txt ]]; then
  rm no_numbers.txt
fi
touch no_numbers.txt
for filen in `ls $ROOTD/$no_FROOT*solverstate`
do
  echo $filen | perl -ne '@l=split("_",$_);@m=split("\\.",@l[4]);print @m[0]."\n"' >> no_numbers.txt
done

touch le_used.txt
touch data_used.txt
touch no_used.txt
