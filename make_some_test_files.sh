#!/bin/bash

# make 100 files with 100 bytes of gibberish
for i in {1..100}
do
  perl -le 'print map { ("a".."z", " ", "\n")[rand 28] } 1..100' > test_file_${i}.dat
done
