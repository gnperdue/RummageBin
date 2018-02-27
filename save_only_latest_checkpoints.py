"""
python <model_directory>

Remove all `checkpoints-N.data-00000-of-00001`, `checkpoints-N.index`, and
`checkpoints-N.meta` except for the largest N from the model_directory.
"""
import os
import sys
import glob
import collections

if '-h' in sys.argv or '--help' in sys.argv:
    print(__doc__)
    sys.exit(1)

dirpath = sys.argv[1]
if sys.argv[1][0] != '/':
    dirpath = os.path.join(os.getcwd(), sys.argv[1])
files = glob.glob(dirpath + '/checkpoints-*.*')

rd = collections.defaultdict(list)
for f in files:
    k = int(f.split('.')[0].split('/')[-1].split('-')[-1])
    rd[k].append(f)

keep_key = sorted(rd.keys())[-1]
rd.pop(keep_key)

for k in rd.keys():
    fs = rd[k]
    for f in fs:
        os.remove(f)
