#!/usr/bin/env python
"""
Usage:
    python find_biggest_caffemodels.py

    Optional args for path, caffemodel string patterns
"""
from __future__ import print_function


if __name__ == '__main__':

    import re
    import os

    from optparse import OptionParser
    parser = OptionParser(usage=__doc__)
    parser.add_option('--le_dann', dest='le_dann',
                      default='50_LE_DANN_2016-09-20T16.08.00.098418_iter_',
                      help='LE DANN file root', metavar='LE_DANN')
    parser.add_option('--no_dann', dest='no_dann',
                      default='50_noDANN_2016-09-10T10.05.03.739066_iter_',
                      help='No DANN file root', metavar='NO_DANN')
    parser.add_option('--data_dann', dest='data_dann',
                      default='50_dataDANN_2016-09-13T21.21.48.709808_iter_',
                      help='Data DANN file root', metavar='DATA_DANN')
    parser.add_option('--path', dest='path', 
                      default='/pnfs/minerva/persistent/users/perdue/Titan/vertex_dann/titan/lustre/atlas/proj-shared/hep105/sohini/vertex/snapshots/',
                      help='Path to caffe models', metavar='PATH')
    (options, args) = parser.parse_args()

    le_dann_pat = re.compile(r'^%s.*caffemodel' % options.le_dann)
    data_dann_pat = re.compile(r'^%s.*caffemodel' % options.data_dann)
    no_dann_pat = re.compile(r'^%s.*caffemodel' % options.no_dann)

    le_max = 0
    data_max = 0
    no_max = 0

    def get_iternum(filename, pattern, current_max):
        m = re.search(pattern, filename)
        if m is not None:
            iternum = int(file.split('_')[-1].split('.')[0])
            if iternum > current_max:
                current_max = iternum
        return current_max

    for root, dirs, files in os.walk(options.path):
        for file in files:
            le_max = get_iternum(file, le_dann_pat, le_max)
            data_max = get_iternum(file, data_dann_pat, data_max)
            no_max = get_iternum(file, no_dann_pat, no_max)

    print(options.path + options.le_dann + str(le_max) +
            '.caffemodel')
    print(options.path + options.data_dann + str(data_max) +
            '.caffemodel')
    print(options.path + options.no_dann + str(no_max) +
            '.caffemodel')
