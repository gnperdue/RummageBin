#!/usr/bin/env python
"""
Usage:
    python ntuple_fixed_size_var_patcher.py <.h file>

This script patches the ntuple header to use the correct "fixed size" vars
for each variable (to get around the effect of calling `MakeClass("mytup")`
on a given ntuple where another may have arrays of larger size).

The script will make a '.bak' file of the original header so you may check
to see if something went wrong in the substitution.

Read comments in the script to see how to update it for new fixed size
variable substitutions.
"""
from __future__ import print_function
import sys
import re
import shutil
import os

# NOTE: To update this script, add a line to `size_var_decl_string` variable.
# Then, add another pattern to the set of patterns below specifying what
# comment to look for in the search (ROOT's `MakeClass()` always adds those
# comments to lines that have "indexed" variables. You need to change three
# lines for each new "fixed-size" variable you want to use - one in the
# string that we'll drop into the header defining the `static const`s and one
# defining a new regular expression to mark lines where you want to execute
# the substitution. Then you need to be sure and add the compiled pattern
# to the list of patterns.

size_var_decl_string = """
   static const size_t MAX_USACT_EXTENT = 250;
   static const size_t MAX_MC_FR_NNUANCESTORIDS = 4*10;
   static const size_t MAX_MC_ER_NPART = 50;
   static const size_t MAX_MC_NFSPART = 25;
   static const size_t MAX_N_PRONGS = 15;
   static const size_t MAX_N_SLICES = 3;
   static const size_t MAX_GENIE_WGT_N_SHIFTS = 7;
   static const size_t MAX_MC_WGT_GENIE_SZ = 100;
   static const size_t MAX_MC_WGT_FLUX_TERTIARY_SZ = 100;
   static const size_t MAX_MC_WGT_FLUX_NA49_SZ = 100;
   static const size_t MAX_MC_WGT_FLUX_BEAMFOCUS_SZ = 100;
"""

# first and last entries of split result are empty strings...
TEMP_STRS = size_var_decl_string.split("\n")[1:-1]
CONSTANTS_STRS = ["[" + x.strip().split()[3] + "]" for x in TEMP_STRS]

# compile regular expressions to search for vars
pattern_MAX_USACT_EXTENT = re.compile(r'//\[usact_extent\]')
pattern_MAX_MC_FR_NNUANCESTORIDS = re.compile(r'//\[mc_fr_nNuAncestorIDs\]')
pattern_MAX_MC_ER_NPART = re.compile(r'//\[mc_er_nPart\]')
pattern_MAX_MC_NFSPART = re.compile(r'//\[mc_nFSPart\]')
pattern_MAX_N_PRONGS = re.compile(r'//\[n_prongs\]')
pattern_MAX_N_SLICES = re.compile(r'//\[n_slices\]')
pattern_MAX_GENIE_WGT_N_SHIFTS = re.compile(r'//\[genie_wgt_n_shifts\]')
pattern_MAX_MC_WGT_GENIE_SZ = re.compile(r'//\[mc_wgt_GENIE_sz\]')
pattern_MAX_MC_WGT_FLUX_TERTIARY_SZ = \
    re.compile(r'//\[mc_wgt_Flux_Tertiary_sz\]')
pattern_MAX_MC_WGT_FLUX_NA49_SZ = re.compile(r'//\[mc_wgt_Flux_NA49_sz\]')
pattern_MAX_MC_WGT_FLUX_BEAMFOCUS_SZ = \
    re.compile(r'//\[mc_wgt_Flux_BeamFocus_sz\]')

CONSTANTS_RES = [
    pattern_MAX_USACT_EXTENT,
    pattern_MAX_MC_FR_NNUANCESTORIDS,
    pattern_MAX_MC_ER_NPART,
    pattern_MAX_MC_NFSPART,
    pattern_MAX_N_PRONGS,
    pattern_MAX_N_SLICES,
    pattern_MAX_GENIE_WGT_N_SHIFTS,
    pattern_MAX_MC_WGT_GENIE_SZ,
    pattern_MAX_MC_WGT_FLUX_TERTIARY_SZ,
    pattern_MAX_MC_WGT_FLUX_NA49_SZ,
    pattern_MAX_MC_WGT_FLUX_BEAMFOCUS_SZ
]

if len(CONSTANTS_RES) != len(CONSTANTS_STRS):
    print("Error - can't extract the number of constants correctly!")
    sys.exit(1)

CONSTANTS_ACTIONS = zip(CONSTANTS_RES, CONSTANTS_STRS)

if __name__ == '__main__':

    if '-h' in sys.argv or '--help' in sys.argv:
        print(__doc__)
        sys.exit(1)

    if not len(sys.argv) == 2:
        print('The header file name argument is mandatory.')
        print(__doc__)
        sys.exit(1)

    # make a .bak in case things go wrong
    fname = sys.argv[1]
    backname = fname + '.bak'
    tempname = fname + '.tmp'
    shutil.copy(fname, backname)

    # write to this file
    wf = open(tempname, 'w')

    # we'll use this to find the digits we want to remove (1st instance)
    pattern_bracket = re.compile(r'\[[0-9]+\]')

    # we'll use this to figure out where to drop the block of consts defs
    pattern_sizes_marker = re.compile(r'//!current Tree number in a TChain')

    with open(fname, 'r') as f:
        for line in f:
            found_a_sub = False
            for patn, strng in CONSTANTS_ACTIONS:
                if patn.search(line):
                    line = pattern_bracket.sub(strng, line)
                    print(line.rstrip(), file=wf)
                    found_a_sub = True
                    break
            if not found_a_sub:
                print(line.rstrip(), file=wf)
                if pattern_sizes_marker.search(line):
                    print(size_var_decl_string, file=wf)

    # close the file and get rid of the temp working file
    wf.close()
    shutil.copy(tempname, fname)
    os.remove(tempname)
