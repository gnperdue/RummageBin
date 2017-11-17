#!/usr/bin/env python
"""
python check_missing_nums.py path min max

look for missing numbers in the sequence of train, valid, test files.
"""
from __future__ import print_function
import sys
import os
import re

if '-h' in sys.argv or '--help' in sys.argv:
    print(__doc__)
    sys.exit(1)

if not len(sys.argv) == 4:
    print(__doc__)
    sys.exit(1)

train_pat = re.compile(
    r'vtxfndingimgs_.*[0-9][0-9][0-9][0-9][0-9][0-9]_train.tfrecord.gz'
)
valid_pat = re.compile(
    r'vtxfndingimgs_.*[0-9][0-9][0-9][0-9][0-9][0-9]_valid.tfrecord.gz'
)
test_pat = re.compile(
    r'vtxfndingimgs_.*[0-9][0-9][0-9][0-9][0-9][0-9]_test.tfrecord.gz'
)
six_digits = re.compile(r'[0-9][0-9][0-9][0-9][0-9][0-9]')

path = sys.argv[1]
min_num = int(sys.argv[2])
max_num = int(sys.argv[3])
ref_list = list(range(min_num, max_num + 1))

train_files = []
valid_files = []
test_files = []


def check_and_add(flist, pat, name):
    m = re.search(pat, name)
    if m is not None:
        flist.append(name)
        return True
    return False


for dpath, dnames, files in os.walk(path):
    for name in files:
        for l, p in zip([train_files, valid_files, test_files],
                        [train_pat, valid_pat, test_pat]):
            if check_and_add(l, p, name):
                continue

for l, s in zip([train_files, valid_files, test_files],
                ['train', 'valid', 'test']):
    n = {int(re.findall(six_digits, f)[0]) for f in l}
    for i in ref_list:
        if i not in n:
            print('missing element {} in {}'.format(i, s))

print('done')
