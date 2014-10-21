#!/bin/bash

FILENAME=$0
if [ $# -gt 0 ]; then
  FILENAME=$1
fi

if [[ -e "$FILENAME" ]]; then
  echo "$FILENAME exists..."
else # == if [[ ! -e "$FILENAME" ]]; then ...
  echo "$FILENAME does not exist."
fi

if [[ -f "$FILENAME" ]]; then
  echo "$FILENAME is a regular file..."
else
  echo "$FILENAME is not a regular file."
fi

if [[ -s "$FILENAME" ]]; then
  echo "$FILENAME is not zero size..."
else
  echo "$FILENAME is zero size."
fi

if [[ -h "$FILENAME" ]]; then
  echo "$FILENAME is a symbolic link..."
else
  echo "$FILENAME is not a symbolic link."
fi

if [[ -d "$FILENAME" ]]; then
  echo "$FILENAME is a directory..."
else
  echo "$FILENAME is not a directory."
fi
