#!/bin/sh

if [[ -z $GENIE ]]; then
    echo Need to set GENIE env var.
    exit 1
fi


SYNAME=$PWD"/.syntastic_cpp_config_genie"

# This script uses the GENIE software environment to create an include paths file for Syntastic.
#  https://github.com/scrooloose/syntastic

# First, remove any existing syntastic config files.
rm -f $SYNAME

# First, get basic GENIE stuff
printenv | grep GENIE | grep -v PATH | perl -ne '@l=split("=",$_);print "-I".@l[1];' >> $SYNAME

# Next, get all the silliness
pushd $GENIE/src  >& /dev/null
echo "-I"${PWD} 1>> $SYNAME
dirlist=`ls`
for dir in $dirlist
do
    cd $dir
    echo "-I"${PWD} 1>> $SYNAME
    cd ..
done

popd >& /dev/null

# Finally, get ROOT - but, we have to go there, otherwise the path ends up confusing syntastic
# (too many ../../'s and softlinks and junk)
RDIR=`printenv | grep ROOTSYS | perl -ne 'chomp $_; @l=split("=",$_); print @l[1]."/include";'`
pushd $RDIR >& /dev/null
ROOTDIR=`pwd`
popd >& /dev/null
echo "-I"$ROOTDIR >> $SYNAME
