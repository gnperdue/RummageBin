#!/usr/bin/env python
"""
Usage:
    python grab_screenshots.py [dest dir name]

Grab all files on the Desktop with names like 'Screen Shot*png' and rename them
such that all ' ' characters are replaced with underscores ('_') and then move
the file to `dest dir name`. If no directory name is specified, the files will
be moved to `.`.
"""
from __future__ import print_function
import os
import re
import sys
import shutil

if '-h' in sys.argv or '--help' in sys.argv:                                       
    print(__doc__)
    sys.exit(1)

destdir = '.'
if len(sys.argv) == 2:
    destdir = sys.argv[1]

basepattern = r'Screen\ Shot.*png'
desktop = os.environ['HOME'] + '/Desktop/'
screenshots = [desktop + f
               for f in os.listdir(desktop)
               if re.match(basepattern, f)]

for s in screenshots:
    shutil.move(s, re.sub(r'\ ', r'_', s))
screenshots = [re.sub(r'\ ', r'_', s) for s in screenshots]
for s in screenshots:
    print("<img src='" + s.split('/')[-1] + "'>")
    shutil.move(s, destdir + '/' + s.split('/')[-1])


