#!/usr/bin/env python
'''
Convert a csv file to a latex table layout.

Usage:
    make_tex.py file.csv
'''

import sys
import csv

if '-h' in sys.argv or '--help' in sys.argv:
    print __doc__
    sys.exit(1)

if not len(sys.argv) == 2:
    print 'The scanfile log argument is mandatory.'
    print __doc__
    sys.exit(1)

filename = sys.argv[1]

# open the csv, get a list of lists, where the innermost items are
# the values separated by commas (and the outermost list is the lines).
# use the universal newline open (being deprecated in Python 3).
ll = list(csv.reader(open(filename, 'rU'), delimiter=','))


for i in range(len(ll)):
    if i == 0:
        print "\\toprule"
    else:
        print "\\midrule"

    line = ll[i]
    stmnt = ''
    for word in line:
        # build the split and swap $ for currency with escaped latex
        stmnt += word.replace('$', '\\$') + ' & '
    # strings are immutable so make a new one that drops the last two
    # chars ('& ') and then add the latex "eol" (\\).
    new_stmnt = stmnt[:-2]
    new_stmnt += '\\\\'
    print new_stmnt

print "\\bottomrule"
