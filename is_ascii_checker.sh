#!/usr/bin/env bash

ARCHDIR=data_archive
mkdir -p $ARCHDIR

for f in `ls *.sql`
do
  # Look for files that are not ASCII
  check=`file $f | grep -v ASCII`
  if [[ $check != "" ]]; then
    # save the output of the check
    echo $check >> report.txt
    # archive the file
    mv $f $ARCHDIR
  fi
done
