#!/bin/bash

logs=`ls *.log`
for logfile in $logs
do
    echo $logfile
    if [[ ! -s $logfile ]]; then
        echo "... is a zero size file, removing!"
        rm $logfile
    fi
done
