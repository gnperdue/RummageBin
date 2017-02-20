#!/bin/sh

DEBUG="gdb -tui --args "
DEBUG=""

nubarfilelistlist="
default_nubar_qe_like_scint.txt
zexp_nubar_qe_like_scint.txt
"

for filelist in $nubarfilelistlist
do
    # cut on the `.` and keep the first part
    fileroot=$(echo $filelist | cut -d. -f1)
    listname=${fileroot}.txt
    rootname=${fileroot}.root
    echo $listname
    echo $rootname
    echo ""
    $DEBUG ../bin/qelikediff -f $listname \
        -o $rootname \
        -m -1 \
        -s -14
done
