#!/usr/bin/env python
"""
take a root directory, a minumum run number, a maximum run number, a minimum
subrun and number, and a maximum subrun number and report all missing sub
runs between the min and max runs. alternatively, supply a file with a list
of runs and subruns (see below)

Usage:
    python find_missing_subruns.py --root "/path/to/files" \
            --min_run 112202 --max_run 112205 --min_sub 1 --max_sub 5000

Or:
    python find_missing_subruns.py --root "/path/to/files" \
            --runs_file "/path/to/playlist"

The `runs_file` or `playist` should be formatted like so:
# RUN  SUBRUN,SUBRUN,...
10068 1,2,3,4,5,6,7,8,9,10,11,12, ...
10069 1,2,3,4,5,6,7,8,9,10, ...

We may supply a comma separated list for the `--root`. We may also pass in
a `tuple` to specify tuple type (default is 'Ana_Tuple'). We may also pass
in a `file_prefix` to specify the leading characters in the file name
(default is 'SIM_minerva' - good alternatives include 'MV', etc.).
"""
from __future__ import print_function


def arg_list_split(option, opt, value, parser):
    """
    split a comma-separated list
    """
    setattr(parser.values, option.dest, value.split(','))


if __name__ == '__main__':

    from collections import defaultdict
    import re
    import os
    import sys

    from optparse import OptionParser
    parser = OptionParser(usage=__doc__)
    parser.add_option('--min_run', dest='min_run', default=0,
                      help='Min run number', metavar='MIN_RUN',
                      type='int')
    parser.add_option('--max_run', dest='max_run', default=0,
                      help='Max run number', metavar='MAX_RUN',
                      type='int')
    parser.add_option('--min_sub', dest='min_sub', default=1,
                      help='Min sub number', metavar='MIN_SUB',
                      type='int')
    parser.add_option('--max_sub', dest='max_sub', default=1,
                      help='Max sub number', metavar='MAX_SUB',
                      type='int')
    parser.add_option('--runs_file', dest='runs_file', type='string',
                      default=None, help='Runs file', metavar='RUNS_FILE')
    parser.add_option('--root', dest='roots', type='string',
                      callback=arg_list_split, help='Root directory',
                      action='callback', metavar='ROOT_DIR')
    parser.add_option('--file_prefix', dest='file_prefix',
                      default='SIM_minerva',
                      help='Ntuple prefix', metavar='NTUPLE_PREFIX')
    parser.add_option('--tuple', dest='tuple_type',
                      default='Ana_Tuple',
                      help='Ntuple type', metavar='TUPLE_TYPE')
    (options, args) = parser.parse_args()

    run_sub_dict = defaultdict(list)
    if options.runs_file is not None:
        with open(options.runs_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line[0] == '#':
                    continue
                run_subs = line.split()
                if len(run_subs) < 2:
                    continue
                run = int(run_subs[0])
                subs = run_subs[1].split(',')
                for sub in subs:
                    run_sub_dict[run].append(int(sub))
    else:
        for run in range(options.min_run, options.max_run + 1):
            for sub in range(options.min_sub, options.max_sub + 1):
                run_sub_dict[run].append(sub)

    ana_tuple_file = re.compile(r'^%s_(\d{8})_.*%s.*\.root$' %
                                (options.file_prefix, options.tuple_type))
    four_digits_plus = re.compile(r'[0-9][0-9][0-9][0-9]+')
    roots = set(options.roots)
    for rootd in roots:
        for root, dirs, files in os.walk(rootd):
            for name in files:
                m = re.search(ana_tuple_file, name)
                if m is not None:
                    # look for all numbers at least 4 digits long
                    numbers = re.findall(four_digits_plus, name)
                    rn = int(numbers[0])
                    if rn in run_sub_dict:
                        for n in numbers[1:]:
                            l = run_sub_dict[rn]
                            try:
                                l.remove(int(n))
                            except ValueError:
                                print(n, "is not in the list")
                                pass
                            run_sub_dict[rn] = l

    for run, subs in run_sub_dict.items():
        if len(subs) > 0:
            sys.stdout.write(str(run) + " ")
            for sub in subs[:-1]:
                sys.stdout.write(str(sub) + ",")
            sys.stdout.write(str(subs[-1]) + "\n")
