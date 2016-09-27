#!/usr/bin/env python
from __future__ import print_function
import subprocess
import tarfile
import gzip
import sys

MAX_BUNDLE=50

if len(sys.argv) > 1:
    MAX_BUNDLE = int(sys.argv[1])

print("tarring", MAX_BUNDLE, "files...") 

ROOTD="/lustre/atlas/proj-shared/hep105/sohini/vertex/snapshots/"
le_FROOT="50_LE_DANN_2016-09-20T16.08.00.098418_iter_"
data_FROOT="50_dataDANN_2016-09-13T21.21.48.709808_iter_"
no_FROOT="50_noDANN_2016-09-10T10.05.03.739066_iter_"

p = subprocess.Popen(['date', '+%s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
dat = int(out)

data_bundle_name = str(dat) + "_dataDANN.tar"
no_bundle_name = str(dat) + "_noDANN.tar"
le_bundle_name = str(dat) + "_leDANN.tar"

def proc_all(nums_file, used_file, bundle_name, froot_name, do_zip=False):
    the_numbers = set()
    with open(nums_file) as f:
        for line in f.readlines():
            the_numbers.add(int(line))
    the_used = set()
    with open(used_file) as f:
        for line in f.readlines():
            the_used.add(int(line))
    the_free = the_numbers - the_used

    num_used = 0
    out = tarfile.open(bundle_name, 'w')
    try:
        for number in the_free:
            cm = ROOTD + froot_name + str(number) + ".caffemodel"
            ss = ROOTD + froot_name + str(number) + ".solverstate"
            print('... archiving ' + cm)
            print('... archiving ' + ss)
            out.add(cm)
            out.add(ss)
            num_used += 1
            with open(used_file, 'a') as f:
                f.write(str(number) + "\n")
            if num_used >= MAX_BUNDLE:
                break
    finally:
        out.close()
    if do_zip:
        print('zipping...')
        f_in = open(bundle_name, 'rb')
        f_out = gzip.open(bundle_name + '.gz', 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
        p = subprocess.Popen(['rm', bundle_name])
        out, err = p.communicate()
        if err is not None:
            print(err)

proc_all('data_numbers.txt', 'data_used.txt', data_bundle_name, data_FROOT)
proc_all('no_numbers.txt', 'no_used.txt', no_bundle_name, no_FROOT)
proc_all('le_numbers.txt', 'le_used.txt', le_bundle_name, le_FROOT)

#data_numbers = set()
#with open('data_numbers.txt') as f:
#    for line in f.readlines():
#        data_numbers.add(int(line))
#data_used = set()
#with open('data_used.txt') as f:
#    for line in f.readlines():
#        data_used.add(int(line))
#data_free = data_numbers - data_used

#num_used = 0
#cmd_string = "-cvzf " + data_bundle_name
#for number in data_free:
#    cm = ROOTD + data_FROOT + str(number) + ".caffemodel"
#    ss = ROOTD + data_FROOT + str(number) + ".solverstate"
#    cmd_string = cmd_string + " " + cm + " " + ss
#    num_used += 1
#    with open('data_used.txt', 'a') as f:
#        f.write(number)
#    if num_used >= MAX_BUNDLE:
#        break
#p = subprocess.Popen('tar', cmd_string, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#out, err = p.communicate()

#no_numbers = set()
#with open('no_numbers.txt') as f:
#    for line in f.readlines():
#        no_numbers.add(int(line))
#no_used = set()
#with open('no_used.txt') as f:
#    for line in f.readlines():
#        no_used.add(int(line))
#no_free = no_numbers - no_used

#le_numbers = set()
#with open('le_numbers.txt') as f:
#    for line in f.readlines():
#        le_numbers.add(int(line))
#le_used = set()
#with open('le_used.txt') as f:
#    for line in f.readlines():
#        le_used.add(int(line))
#le_free = le_numbers - le_used

#for n in le_numbers:
#    print(n)
