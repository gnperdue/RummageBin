#!/usr/bin/env python
"""
Mining a file with lines like:
    $ head mnv1.txt 
       0        5 ; module+5 = 0; plane = 1; bucket = 0; view =  1
       1        8 ; module+5 = 0; plane = 2; bucket = 0; view =  0
and collecting the number in the `view = N` part. View is only ever {0, 1, 2}.
"""
from __future__ import print_function
import re


plane_counter = {'0': 0, '1': 0, '2': 0}
with open("mnv1.txt", "r") as f:
    for line in f:
        # check for lines containing "data"
        if re.search(";", line):
            # strip newline and split by `;`
            bits = line.rstrip().split(';')
            viewstr = bits[-1]
            view = viewstr[-1]
            # build up the counter dictionary
            plane_counter[view] += 1

print(plane_counter)
