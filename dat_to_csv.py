#!/usr/bin/env python
"""
Usage:
    python dat_to_csv.py <filename>

NOTE: This file ASSUMES the orignal file is not a `.csv` file. It will create
a .csv file with the same basename as the original file. If the orignal file
already had a .csv name extension, this program will overwrite that file.

This program further assumes there is only one '.' in the filename.
"""
from __future__ import print_function
import sys
import shutil
import re

if '-h' in sys.argv or '--help' in sys.argv:
    print(__doc__)
    sys.exit(1)

if len(sys.argv) != 2:
    print("Error! You must supply a file name.")
    print(__doc__)
    sys.exit(1)

filename = sys.argv[1]
basename = filename.split('.')[0]
newfilename = basename + '.tmp'
csvfilename = basename + '.csv'

data_pattern = re.compile(r'\s+([0-9]+\.*[0-9]*)\s+([0-9]+\.*[0-9]*)\s+')

with open(filename, 'r') as source:
    lines = source.readlines()
    with open(newfilename, 'w') as dest:
        for line in lines:
            if line[0] == "#":
                dest.write(line)
            else:
                m = data_pattern.search(line)
                if m is None:
                    continue
                num1 = float(m.groups()[0])
                num2 = float(m.groups()[1])
                dest.write('{:0.3f}, {:0.3f}\n'.format(num1, num2))

shutil.move(newfilename, csvfilename)
