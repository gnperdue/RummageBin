#!/bin/bash

# The real original $filelist was much, much longer.
# Capture the filelist with `ls -1`, slap it into a var, and then do a sub
# like so... Move just a subset of files buried in very deep paths into
# something "similar" but with a slightly modified directory near the
# trunk of the path

filelist="
/minerva/data/users/perdue/mc_ana_minervame1A_20150925/grid/central_value/minerva/ana/v10r8p7/00/00/00/01/SIM_minerva_00000001_Subruns_0000-0001-0002-0003-0004_MLVFSamplePrepTool_Ana_Tuple_v10r8p7-perdue.root
/minerva/data/users/perdue/mc_ana_minervame1A_20150925/grid/central_value/minerva/ana/v10r8p7/00/00/00/02/SIM_minerva_00000002_Subruns_0000-0001-0002_MLVFSamplePrepTool_Ana_Tuple_v10r8p7-perdue.root
/minerva/data/users/perdue/mc_ana_minervame1A_20150925/grid/central_value/minerva/ana/v10r8p7/00/00/00/03/SIM_minerva_00000003_Subruns_0000-0001-0002-0003-0004_MLVFSamplePrepTool_Ana_Tuple_v10r8p7-perdue.root
"

for file in $filelist
do
    filen=$(basename $file)
    dirn=$(dirname $file)
    dirn=`echo $dirn | perl -pi -e 's/mc_ana_minervame1A_20150925/mc_production_ml_vertex_20150925/g'`
    mkdir -p $dirn
    mv $file $dirn/$filen
done
