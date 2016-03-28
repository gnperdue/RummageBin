#!/usr/bin/env python
from __future__ import print_function
import sys
import shutil
import random

fname = sys.argv[1]
with open(fname, 'r') as f:
    lines = f.readlines()

shutil.move(fname, fname + '.bak')
first = lines[0]
rest = lines[1:]
random.shuffle(rest)
newlines = [first] + rest
with open(fname, 'w') as f:
    for line in newlines:
        f.write(line)
