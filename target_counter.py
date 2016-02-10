#!/usr/bin/env python
"""
Usage:
    python target_counter file.dat
"""
from __future__ import print_function


if __name__ == '__main__':
    import sys
    from collections import defaultdict

    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) == 1:
        print(__doc__)
        sys.exit(1)

    fname = sys.argv[1]
    segments = defaultdict(int)
    with open(fname, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split()[0]
            if data != '#':
                segments[data] += 1

    for k, v in segments.iteritems():
        print("Segment", k, ":", v)
