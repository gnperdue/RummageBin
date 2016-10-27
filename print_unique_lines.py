#!/usr/bin/env python
from __future__ import print_function
import sys

fname = sys.argv[1]
with open(fname, 'r') as f:
    lines = f.readlines()
    set_lines = set(lines)
    for n in set_lines:
        print(n.strip())
