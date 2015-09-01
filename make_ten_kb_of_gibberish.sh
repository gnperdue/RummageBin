#!/bin/bash
perl -le 'print map { ("a".."z", " ", "\n")[rand 28] } 1..10240' > ten_kb_file.dat
