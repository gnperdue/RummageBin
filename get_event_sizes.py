#!/usr/bin/env python
from __future__ import print_function
import os
import re
import sys

excluded_patterns = [
    re.compile(r'(.*)segments_bal(.*)'),
    re.compile(r'(.*)targets_bal(.*)')
]
hitimes_shape_pat = re.compile(r'([0-9]+, 2, 127, 47)')


def enumerate_files(path, keystring):
    '''
    Get a list of all files under `path` containing the string `keystring` and
    don't include an excluded pattern.
    '''
    file_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            skip = False
            for pat in excluded_patterns:
                if re.match(pat, filename):
                    skip = True
                    break
            if not skip and re.match(keystring, filename):
                fullpath = os.path.join(dirpath, filename)
                file_collection.append(fullpath)

    return file_collection


dirpath = sys.argv[1]
files = enumerate_files(dirpath, r'(.*)README.txt')

evt_nums_dict = {}
for f in files:
    fname = f.split('/')[-1]
    plist = fname.split('_')[2]
    evt_nums_dict[plist] = {}
    evt_nums_dict[plist]['file'] = f
    with open(f, 'r') as of:
        lines = of.readlines()
        for line in lines:
            m = re.search(hitimes_shape_pat, line)
            if m is not None:
                shp = re.findall(hitimes_shape_pat, line)[0]
                nmbr = int(shp.split(',')[0])
                evt_nums_dict[plist]['count'] = nmbr

ks = evt_nums_dict.keys()
ks_data = []
ks_mc = []
for k in ks:
    if 'data' in k:
        ks_data.append(k)
    else:
        ks_mc.append(k)

ks_data = sorted(ks_data)
ks_mc = sorted(ks_mc)
print(ks_data)
print(ks_mc)

for k in ks_data:
    print(k, evt_nums_dict[k]['count'])

for k in ks_mc:
    print(k, evt_nums_dict[k]['count'])
