#!/usr/bin/env python
"""
Count missing subruns per run.
"""
import sys

if '-h' in sys.argv or '--help' in sys.argv:
    print(__doc__)
    sys.exit(1)

if not len(sys.argv) == 2:
    print('The missing subs file argument is mandatory.')
    print(__doc__)
    sys.exit(1)

filename = sys.argv[1]

f = open(filename, 'r')
lines = f.readlines()
tot_missing_subs = 0
for line in lines:
    parts = line.split(' ')
    run = parts[0]
    subs = parts[1].split(',')
    nsubs = len(subs)
    tot_missing_subs += nsubs
    print run, nsubs

print tot_missing_subs

f.close()
