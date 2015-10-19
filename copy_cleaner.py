#!/usr/bin/env python
"""
Clean out the redundant files that are downloaded when I sync my Manning books.
"""
from __future__ import print_function
import os


def enumerate_files(path, keystring):
    '''
    Get a list of all files under `path` containing the string `keystring`.
    '''
    import re

    file_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if re.match(keystring, filename):
                fullpath = os.path.join(dirpath, filename)
                file_collection.append(fullpath)

    return file_collection


if __name__ == '__main__':

    dpath = r'/Users/perdue/Dropbox/Apps/Manning Books'
    search_string = r'(.*)\(1\)(.*)'

    files = enumerate_files(dpath, search_string)
    for file in files:
        os.remove(file)
