#!/bin/bash
perl -le 'print map { ("a".."z", " ", "\n")[rand 28] } 1..10240' > ten_kb_file.dat

# just 8 random numbers, etc.
# perl -le 'print map { ("0".."9")[rand 10] } 1..8' > file.dat
