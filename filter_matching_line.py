#!/usr/bin/env python
import re
import os


the_file = open("logf.txt", "r")
for line in the_file:
    if re.match("(.*)gnptemp(.*)", line):
        print(line.rstrip(os.linesep))
