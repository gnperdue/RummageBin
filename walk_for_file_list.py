#!/usr/bin/env python

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


def write_list_of_files_to_file(list_of_files, filenam):
    with open(filenam, 'w') as f:
        for file in list_of_files:
            print(file, file=f)


if __name__ == '__main__':

    data_path  = '/pnfs/minerva/scratch/users/minervapro'
    data_path += '/mc_production_genie_DFR_v10r8p4/grid/central_value/minerva'
    data_path += '/genie/v10r8p4/00/01/00/00/'

    search_string = r'(.*)v10r8p4_DFR_ghep(.*)'

    files = enumerate_files(data_path, search_string)
    write_list_of_files_to_file(files, 'diffractive_events_file_list.txt')
