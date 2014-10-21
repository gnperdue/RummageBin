#!/bin/bash

FILENAME=$0
if [ $# -gt 0 ]; then
  FILENAME=$1
fi

if [[ -e "$FILENAME" ]]; then
  echo "$FILENAME exists..."
fi

if [[ -f "$FILENAME" ]]; then
  echo "$FILENAME is a regular file..."
fi

if [[ -s "$FILENAME" ]]; then
  echo "$FILENAME is not zero size..."
fi


