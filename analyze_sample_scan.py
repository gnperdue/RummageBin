#!/usr/bin/env python
"""
analyze_sample_scan scanfile.log

This program assumes the scanfile.log was produced by the run_validation.sh
script. This means the content of the file is expected to look like so:

    Analyzing file gntp.1002.ghep.root...
    --------------------
    1407444969 ERROR gvldtest : [n] <gVldSampleScan.cxx::main (209)> : \
        ** s is not conserved at this event
    1407444969 ERROR gvldtest : [n] <gVldSampleScan.cxx::main (212)> :
    1407444969 ERROR gvldtest : [n] <gVldSampleScan.cxx::main (213)> :
"""

from __future__ import print_function
import sys
import re

if '-h' in sys.argv or '--help' in sys.argv:
    print(__doc__)
    sys.exit(1)

if not len(sys.argv) == 2:
    print('The scanfile log argument is mandatory.')
    print(__doc__)
    sys.exit(1)

filename = sys.argv[1]

run_dictionary = {
    '1000': {'evts': 100000, 'desc': 'numu    + n',
             'energy': 0.5, 'channels': 'all'},
    '1001': {'evts': 100000, 'desc': 'numu    + n',
             'energy':   1, 'channels': 'all'},
    '1002': {'evts': 100000, 'desc': 'numu    + n',
             'energy':   5, 'channels': 'all'},
    '1003': {'evts': 100000, 'desc': 'numu    + n',
             'energy':  50, 'channels': 'all'},
    '1101': {'evts': 100000, 'desc': 'numubar + p',
             'energy':   1, 'channels': 'all'},
    '1102': {'evts': 100000, 'desc': 'numubar + p',
             'energy':   5, 'channels': 'all'},
    '1103': {'evts': 100000, 'desc': 'numubar + p',
             'energy':  50, 'channels': 'all'},
    '2001': {'evts': 100000, 'desc': 'numu    + Fe56',
             'energy':  1, 'channels': 'all'},
    '2002': {'evts': 100000, 'desc': 'numu    + Fe56',
             'energy':  5, 'channels': 'all'},
    '2003': {'evts': 100000, 'desc': 'numu    + Fe56',
             'energy': 50, 'channels': 'all'},
    '2101': {'evts': 100000, 'desc': 'numubar + Fe56',
             'energy':  1, 'channels': 'all'},
    '2102': {'evts': 100000, 'desc': 'numubar + Fe56',
             'energy':  5, 'channels': 'all'},
    '2103': {'evts': 100000, 'desc': 'numubar + Fe56',
             'energy': 50, 'channels': 'all'},
    '9001': {'evts': 100000, 'desc': 'numu    + Fe56',
             'energy':  5, 'channels': 'DIS charm'},
    '9002': {'evts': 100000, 'desc': 'numu    + Fe56',
             'energy':  5, 'channels': 'QEL charm'},
    '9101': {'evts': 100000, 'desc': 'numu    + Fe56',
             'energy':  2, 'channels': 'COH CC+NC'},
    '9201': {'evts': 100000, 'desc': 'nue     + Fe56',
             'energy':  1, 'channels': 've elastic'},
    '9202': {'evts': 100000, 'desc': 'numu    + Fe56',
             'energy':  1, 'channels': 've elastic'},
    '9203': {'evts':  50000, 'desc': 'numu    + Fe56',
             'energy': 20, 'channels': 'IMD'},
    '9204': {'evts':  50000, 'desc': 'nuebar  + Fe56',
             'energy': 20, 'channels': 'IMD (annihilation)'}
}

results = {}
filenum = 0

with open(filename, 'r') as f:

    for line in f:
        line = line.rstrip()

        if re.match("Analyzing file", line):
            words = line.split()
            gntp = words[2]
            filenum = gntp.split('.')[1]

        if re.search("is not conserved", line):
            error = line.split(':')[-1]
            if error in results:
                d = results[error]
                if filenum in d:
                    d[filenum] += 1
                else:
                    d[filenum] = 1
            else:
                results[error] = {filenum: 1}


print(results)

for error in results:
    nerror = 0
    nevt = 0
    for run in results[error]:
        runnum = run
        nerror += results[error][run]
        if runnum in run_dictionary:
            descr = run_dictionary[runnum]
            nevt += descr['evts']
    print("%s: %d / %d = %f" %
          (error, nerror, nevt, float(nerror)/nevt))
