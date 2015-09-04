#!/usr/bin/env python
"""
Take a LaTeX file marked up with red changes (e.g., using {\color{red} text}
to color "changed" text red) and with strikeouts (e.g., \sout{text}) and remove
those "highlights" that mark a change (but keep the change itself).

Usage:
    python remove_markup.py <latex file>
"""
from __future__ import print_function

if __name__ == '__main__':
    import re
    import sys
    import shutil
    import os

    if '-h' in sys.argv or '--help' in sys.argv:
        print(__doc__)
        sys.exit(1)

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)

    fname = sys.argv[1]
    backname = fname + '.bak'
    tempname = fname + '.tmp'
    shutil.copy(fname, backname)

    wf = open(tempname, 'w')
    
    with open(sys.argv[1], "r") as f:
        # first, we want to remove all strikeouts
        # build a regex that looks for `\sout{}` with the minimum number
        # of (any sort of character) between the `{}`'s - get the 1st `}`
        pattern_sout = re.compile(r"\\sout\{.*?\}")
        # next, remove all empty `{\color{red} }` blocks
        # build a rege that looks for `{\color{red} }` with only space
        # inside.
        pattern_empty_color = re.compile(r"\{\\color\{red\}\s*?\}")
        # next, remove all the `{\color{red} text}` blocks but leave the
        # "text" part behind.
        pattern_red_text = re.compile(r"\{\\color\{red\}(.*?)\}")
        # finally, remove double-spaces, just to clean up
        pattern_double_space = re.compile(r"\s(\s)+")

        for line in f:
            if pattern_sout.search(line):
                line = pattern_sout.sub(r"", line)
                
            if pattern_empty_color.search(line):
                line = pattern_empty_color.sub(r"", line)
                
            m = pattern_red_text.search(line)
            while m:
                line = pattern_red_text.sub(m.group(1), line, count=1)
                m = pattern_red_text.search(line)

            if pattern_double_space.search(line):
                line = pattern_double_space.sub(r" ", line)

            print(line.strip(), file=wf)

    wf.close()
    shutil.copy(tempname, fname)
    os.remove(tempname)
