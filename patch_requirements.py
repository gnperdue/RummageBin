#!/usr/bin/env python
"""
Patch the requirements file with the appropriate version and tag.

Examples:

    python patch_requirements.py -v v19 -t v19p3_prl
    python patch_requirements.py --version v19 --tag v19p3_prl

The 'version' is the ntuple version (default v19), and the tag codes the plots
version (default v19p3_prl).
"""

from __future__ import print_function
import re

version_help = 'Ntuple version'
tag_help = 'Histogram and plots version'


def patch_file(filenam, version, tag):
    """
    Patch the `version` and `tag` values into file `filenam`.
    """
    # don't include newlines in the search strings
    SEARCH_VERSION = r'set NUKECC_V .*'
    SEARCH_TAG = r'set NUKECC_TAG .*'

    with open(filenam, 'r+') as f:
        # load the contents of the requirements file into memory
        contents = f.read()

        # compile regular expressions to find the VERSION and TAG
        pattern_version = re.compile(SEARCH_VERSION)
        pattern_tag = re.compile(SEARCH_TAG)

        # set up replacement strings for the current VERSION and TAG
        replace_version = 'set NUKECC_V ' + version + '  # ' + version_help
        replace_tag = 'set NUKECC_TAG ' + tag + '  # ' + tag_help

        # substitute the new values for the old
        contents = pattern_version.sub(replace_version, contents)
        contents = pattern_tag.sub(replace_tag, contents)

        # go back to the beginning of the file and clear the contents
        f.seek(0)
        f.truncate()

        # write the data in memory back into the file
        f.write(contents)


if __name__ == '__main__':

    from optparse import OptionParser
    parser = OptionParser(usage=__doc__)
    parser.add_option('-v', '--version', dest='version', default='v19',
                      help=version_help, metavar='NTUPLE VERSION')
    parser.add_option('-t', '--tag', dest='tag', default='v19p3_prl',
                      help=tag_help,
                      metavar='PLOTS VERSION')
    (options, args) = parser.parse_args()

    patch_file("./requirements", options.version, options.tag)
