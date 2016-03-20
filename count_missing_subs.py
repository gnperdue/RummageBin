#!/usr/bin/env python
f = open('missing_me1A.txt', 'r')
lines = f.readlines()
tot_missing_subs = 0
for line in lines:
    parts = line.split(' ')
    run = parts[0]
    subs = parts[1].split(',')
    nsubs = len(subs)
    tot_missing_subs += nsubs
    print run, nsubs

print tot_missing_subs

f.close()
