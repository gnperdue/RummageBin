#!/usr/bin/env python3
"""
This program counts the words in a list of text files. Usage:

    python3 count_words.py file1 file2 file3 ...
"""
import sys
from collections import Counter
from pprint import pprint

if __name__ == '__main__':

    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) == 1:
        print(__doc__)
        sys.exit(1)
    
    file_list = sys.argv[1:]

    cnt = Counter()
    
    for filename in file_list:
        with open(filename, 'r') as f:
            for line in f:
                words = line.split()
                for word in words:
                    cnt[word] += 1

    pprint(cnt.most_common(20))
