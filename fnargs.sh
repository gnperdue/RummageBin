#!/bin/sh

test() {
  echo "Number of args: $#"
  if [ $# -gt 0 ]; then
    echo "All arguments: $@"
    for arg in $@; do
      echo "One at a time... $arg"
    done
    echo "First arg: $1"
  fi
  if [ $# -gt 1 ]; then
    echo "Second arg: $2"
  fi
  if [ $# -gt 2 ]; then
    echo "Third arg: $3"
  fi
  if [ $# -eq 3 ]; then
    echo "There were exactly three arguments."
  fi
}

test 1 2 3

