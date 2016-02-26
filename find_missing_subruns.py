#!/usr/bin/env python
"""
take a root directory, a minumum run number, a maximum run number, a minimum
subrun and number, and a maximum subrun number and report all missing sub
runs between the min and max runs

currently - look only for ROOT files in the pattern SIM_minerva_...Ana_Tuple;
TODO: let the user pass in the lead part of the file string so this could
work with other file types, etc.

Usage:
    python find_missing_subruns.py --root "/path/to/files" \
            --min_run 112202 --max_run 112205 --min_sub 1 --max_sub 5000
"""
from __future__ import print_function

if __name__ == '__main__':

    from collections import defaultdict
    import re
    import os
    import sys

    from optparse import OptionParser
    parser = OptionParser(usage=__doc__)
    parser.add_option('--min_run', dest='min_run', default=112200,
                      help='Min run number', metavar='MIN_RUN',
                      type='int')
    parser.add_option('--max_run', dest='max_run', default=112200,
                      help='Max run number', metavar='MAX_RUN',
                      type='int')
    parser.add_option('--min_sub', dest='min_sub', default=1,
                      help='Min sub number', metavar='MIN_SUB',
                      type='int')
    parser.add_option('--max_sub', dest='max_sub', default=5000,
                      help='Max sub number', metavar='MAX_SUB',
                      type='int')
    parser.add_option('--root', dest='root',
                      default='/minerva/data/users',
                      help='Root directory', metavar='ROOT_DIR')
    (options, args) = parser.parse_args()

    run_sub_dict = defaultdict(list)
    for run in range(options.min_run, options.max_run + 1):
        for sub in range(options.min_sub, options.max_sub + 1):
            run_sub_dict[run].append(sub)

    ana_tuple_file = re.compile(r'^SIM_minerva_(\d{8})_.*Ana_Tuple.*\.root$')
    four_digits_plus = re.compile(r'[0-9][0-9][0-9][0-9]+')
    for root, dirs, files in os.walk(options.root):
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
        sys.stdout.write(str(run) + " ")
        for sub in subs[:-1]:
            sys.stdout.write(str(sub) + ",")
        sys.stdout.write(str(subs[-1]) + "\n")
