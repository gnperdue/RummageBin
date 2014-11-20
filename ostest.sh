#!/usr/bin/env bash

MKTEMPC=gmktemp
OS=`uname`
if [[ $OS == "Darwin" ]]; then
  MKTEMPC=gmktemp
else
  MKTEMPC=mktemp
fi
echo "Using $MKTEMPC"

if [ -z "$TMPDIR" ]; then
  TMPDIR=/tmp/
fi
IN=$($MKTEMPC ${TMPDIR}Test-XXXXXXXX)
OUT=$($MKTEMPC ${TMPDIR}Test-XXXXXXXX).png
ERR=$($MKTEMPC ${TMPDIR}Test-XXXXXXXX).err
echo "$IN"
echo "$OUT"
echo "$ERR"

