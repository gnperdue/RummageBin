#!/usr/bin/env python
from __future__ import print_function
import sys

fname1 = sys.argv[1]
fname2 = sys.argv[2]

fset1 = set()
fset2 = set()

with open(fname1, 'r') as f:
    for line in f.readlines():
        line = line.strip()
        fset1.add(line)

with open(fname2, 'r') as f:
    for line in f.readlines():
        line = line.strip()
        fset2.add(line)

print("size of set 1 = %d" % len(fset1))
print("size of set 2 = %d" % len(fset2))

remset = fset1 - fset2
for n in remset:
    print(n)
