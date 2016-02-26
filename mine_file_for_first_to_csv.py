#!/usr/bin/env python
"""
read a file and make a one-line csv from the first entry of every line in the
file
"""
import sys
fname = sys.argv[1]
with open(fname, 'r') as f:
    for line in f.readlines():
        jobid = line.split()[0]
        sys.stdout.write(jobid + ",")
