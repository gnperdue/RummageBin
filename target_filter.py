#!/usr/bin/env python
"""
Usage:
    python target_filter -f skim_file.dat -t target1,target2,...

This script filters through a libsvm/liblinear .dat file and replaces the
first _character_ with 0 if it is not equal to target1, target2, etc.
This assumes less than 10 targets, which is a safe assumption in Minerva.

The script will first copy the data file into a .bak file, and then it
will modify the contents of the original file in-place.
"""

def arg_list_split(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))


if __name__ == '__main__':
    from optparse import OptionParser
    import shutil
    import sys

    parser = OptionParser(usage=__doc__)
    parser.add_option('-f', type='string', help=r'Data file', dest='fname')
    parser.add_option('-t', type='string', action='callback', dest='targs',
            callback=arg_list_split)
    (options, args) = parser.parse_args()

    if options.fname is None or options.targs is None:
        print(__doc__)
        sys.exit(1)

    shutil.move(options.fname, options.fname + '.bak')
    targets = set(options.targs)

    destination = open(options.fname, "w")
    source = open(options.fname + '.bak', "r")
    for line in source:
        if line[0] not in targets:
            line = '0' + line[1:]
        destination.write(line)
    source.close()
    destination.close()
