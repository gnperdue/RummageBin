#!/bin/sh

# This script uses the Minerva software environment to create an include paths file for Syntastic.
#  https://github.com/scrooloose/syntastic
# First it gets all the "MINERVA" environment variables, then it filters out all non "ROOT" variables 
# (Gaudi convention), then it excludes the PATH, and finally it pipes the output through a perl command
# that splits on the '=' and drops the first part (the actual environment variable name itself).

# First, remove any existing syntastic config files.
rm -f .syntastic_cpp_config
# Next, create our new config file.
# First, get the base install dirs 
printenv | grep MINERVA | grep ROOT | grep -v PATH | perl -ne 'while (<>){@l=split("=",$_);print "-I".@l[1];}' >> .syntastic_cpp_config
# Second, get the cmt user area stuff
printenv | grep Minerva_ | grep ROOT | grep -v PATH | perl -ne 'while (<>){@l=split("=",$_);print "-I".@l[1];}' >> .syntastic_cpp_config
