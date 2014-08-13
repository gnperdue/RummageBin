#!/bin/sh

DO_HADRO="no"
DO_SAMPS="no"
DO_SPLCH="no"
DO_EVSMP="no"
DO_EXDTA="no"
DO_SFCMP="no"
DO_ALL="no"

help() {
  echo "Usage: ./run_validation.sh -<flags>"
  echo "                 -a    : All tests"
  echo "                 -h    : Hadronization"
  echo "                 -s    : Sample scan"
  echo "                 -p    : Spline check"
  echo "                 -e    : Event sample comparison"
  echo "                 -d    : External data comparison"
  echo "                 -f    : Spectral function comparison"
  echo " "
}

# The files available in the validation samples tarball:
#   v2.8.2-release_test_01.tar.gz
# were as follows:
# ------------------------------------------------------
# $ tree
# .
# |-- flux
# |-- geom
# |-- hadronization
# |   `-- ghep
# |       |-- gntp.100000.ghep.root
# |       |-- gntp.110000.ghep.root
# |       |-- gntp.120000.ghep.root
# |       `-- gntp.130000.ghep.root
# |-- intranuke
# |   `-- ghep
# |-- mctest
# |   |-- ghep
# |   |   |-- gntp.1000.ghep.root
# |   |   |-- gntp.1001.ghep.root
# |   |   |-- gntp.1002.ghep.root
# |   |   |-- gntp.1003.ghep.root
# |   |   |-- gntp.1101.ghep.root
# |   |   |-- gntp.1102.ghep.root
# |   |   |-- gntp.1103.ghep.root
# |   |   |-- gntp.2001.ghep.root
# |   |   |-- gntp.2002.ghep.root
# |   |   |-- gntp.2003.ghep.root
# |   |   |-- gntp.2101.ghep.root
# |   |   |-- gntp.2102.ghep.root
# |   |   |-- gntp.2103.ghep.root
# |   |   |-- gntp.9001.ghep.root
# |   |   |-- gntp.9002.ghep.root
# |   |   |-- gntp.9101.ghep.root
# |   |   |-- gntp.9201.ghep.root
# |   |   |-- gntp.9202.ghep.root
# |   |   |-- gntp.9203.ghep.root
# |   |   `-- gntp.9204.ghep.root
# |   `-- gst
# |       |-- gntp.1000.gst.root
# |       |-- gntp.1001.gst.root
# |       |-- gntp.1002.gst.root
# |       |-- gntp.1003.gst.root
# |       |-- gntp.1101.gst.root
# |       |-- gntp.1102.gst.root
# |       |-- gntp.1103.gst.root
# |       |-- gntp.2001.gst.root
# |       |-- gntp.2002.gst.root
# |       |-- gntp.2003.gst.root
# |       |-- gntp.2101.gst.root
# |       |-- gntp.2102.gst.root
# |       |-- gntp.2103.gst.root
# |       |-- gntp.9001.gst.root
# |       |-- gntp.9002.gst.root
# |       |-- gntp.9101.gst.root
# |       |-- gntp.9201.gst.root
# |       |-- gntp.9202.gst.root
# |       |-- gntp.9203.gst.root
# |       `-- gntp.9204.gst.root
# |-- reports
# |-- reptest
# |   `-- ghep
# |       `-- gntp.0.ghep.root
# |-- reweight
# |-- xsec
# |   |-- gxspl-vA-v2.8.2.xml
# |   |-- gxspl-vN-v2.8.2.xml
# |   `-- xsec.root
# `-- xsec_validation
#     |-- file_list.xml
#     |-- ghep
#     |   |-- gntp.100000.ghep.root
#     |   |-- gntp.110000.ghep.root
#     |   |-- gntp.120000.ghep.root
#     |   |-- gntp.130000.ghep.root
#     |   `-- gntp.201000.ghep.root
#     `-- gst
#         |-- gntp.100000.gst.root
#         |-- gntp.110000.gst.root
#         |-- gntp.120000.gst.root
#         |-- gntp.130000.gst.root
#         `-- gntp.201000.gst.root
#
# 17 directories, 59 files


# `gvld_sample_scan`  Check two files, one on a free nucleon, and one on a nucleus.
# Here we assume that file numbers like 1XXX are free nucleon, and numbers like 2XXX 
# are on iron. (Probably not important.)
do_gvld_sample_scan() {
  WORKDIR=$VALIDROOT/mctest/ghep
  REPFILE=$VALIDREPS/gvld_sample_scan.log
  rm -f $REPFILE
  echo "REPFILE = $REPFILE"
  pushd $WORKDIR >& /dev/null

  files=($(ls gntp*root))
  for f in "${files[@]}"
  do
    gvld_sample_scan -f $f --check-energy-momentum-conservation \
    --check-for-pseudoparticles-in-final-state \
    --check-for-off-mass-shell-particles-in-final-state \
    --check-for-num-of-final-state-nucleons-inconsistent-with-target \
    >& tmp.txt
    echo "Analyzing file $f..." >> $REPFILE
    echo "--------------------" >> $REPFILE
    grep -i error tmp.txt >> $REPFILE
    grep -i warn tmp.txt >> $REPFILE
  done

  popd >& /dev/null
}

# `gvld_hadronz_test` - Run the hadronization validation program.
# Make a "hadronization.xml" file by getting the list of run numbers 
# from the hadronization/ghep directory (using a crude `cut` that is 
# relying on a specific file-naming convention, namely that the files 
# appear like:
#       gntp.######.ghep.root
# and the `#` characters specify the run number. Then push to the 
# directory and run the validation program.
do_gvld_hadronz_test() {
  HADRODIR=$VALIDROOT/hadronization/ghep/
  HADROOUT=$VALIDREPS/hadronization
  pushd $HADRODIR >& /dev/null

  # build the input xml file on the fly
  echo "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>" > hadronization.xml
  echo "<genie_simulation_outputs>" >> hadronization.xml
  echo "<model name=\"GENIE SVN 2.8.0\">" >> hadronization.xml
  runnumbers=($(ls gntp*root | cut -c6-11))
  for i in "${runnumbers[@]}"
  do
    echo "<evt_file format=\"ghep\"> ./gntp.$i.ghep.root </evt_file>" >> hadronization.xml
  done
  echo "</model>" >> hadronization.xml
  echo "</genie_simulation_outputs>" >> hadronization.xml

  # run the validation
  echo "gvld_hadronz_test -g hadronization.xml -f gif"
  gvld_hadronz_test -g hadronization.xml -f gif

  # save the gifs if possible
  if [ ! -d $HADROOUT ]; then
    mkdir -p $HADROOUT
  fi
  if [ -d $HADROOUT ]; then
    mv *.gif $HADROOUT
  fi
  popd >& /dev/null
}

# `gvld_xsec_comp` - The spline checking program.
do_gvld_xsec_comp() {
  pushd xsec >& /dev/null
  INFILE=$VALIDROOT/xsec/xsec.root
  COMPFILE=$VALIDROOT/xsec/xsec.root
  echo "gvld_xsec_comp -f $INFILE -r $COMPFILE"
  gvld_xsec_comp -f $INFILE -r $COMPFILE
  mv gxsec.ps $VALIDREPS
  popd >& /dev/null 
}

# The event sample comparison program.
do_gvld_sample_comp() {
  EVOUT=$VALIDREPS/event_sample
  pushd xsec_validation/ghep >& /dev/null
  runnumbers=($(ls gntp*root | cut -c6-11))
  OLDVALIDPATH=/minerva/app/users/perdue/GENIE/validation/v2.8.0
  for i in "${runnumbers[@]}"
  do
    INFILE=gntp.$i.ghep.root
    REFFLAGFILE="$OLDVALIDPATH/xsec_validation/ghep/$INFILE"
    if [ -f $REFFLAGFILE ]; then 
      echo "Checking run $i"
      gvld_sample_comp -f $INFILE -r $REFFLAGFILE
    fi
  done

  # save the output if possible
  if [ ! -d $EVOUT ]; then
    mkdir -p $EVOUT
  fi
  if [ -d $EVOUT ]; then
    mv *.ps $EVOUT
  fi
  popd >& /dev/null
}

# The comparison to external data program.
do_gvld_nu_xsec() {
  pushd xsec_validation >& /dev/null
  INFILE=vldxsec.xml
  echo "gvld_nu_xsec -g $INFILE"
  gvld_nu_xsec -g $INFILE
  popd >& /dev/null
}

# The structure function comparison program.
do_gvld_sf() {
  echo "gvld_sf --resonance-xsec-model genie::ReinSeghalRESPXSec/Default" 
  echo "        --dis-xsec-model genie::QPMDISPXSec/Default"
  echo "        --dis-charm-xsec-model genie::AivazisCharmPXSecLO/CC-Default"
  gvld_sf --resonance-xsec-model genie::ReinSeghalRESPXSec/Default \
  --dis-xsec-model genie::QPMDISPXSec/Default \
  --dis-charm-xsec-model genie::AivazisCharmPXSecLO/CC-Default
  mv genie-structfunc*ps $VALIDREPS
}

help() {
  echo "Usage: ./run_validation.sh -<flags>"
  echo "                 -a    : All tests"
  echo "                 -h    : Hadronization"
  echo "                 -s    : Sample scan"
  echo "                 -p    : Spline check"
  echo "                 -e    : Event sample comparison"
  echo "                 -d    : External data comparison"
  echo "                 -f    : Structure function comparison"
  echo " "
}

while getopts "ahspedf" options; do
  case $options in
    a) DO_ALL="yes";;
    h) DO_HADRO="yes";;
    s) DO_SAMPS="yes";;
    p) DO_SPLCH="yes";;
    e) DO_EVSMP="yes";;
    d) DO_EXDTA="yes";;
    f) DO_SFCMP="yes";;
  esac
done

if [ "$#" -eq 0 ]; then
  help
  exit 0
fi 

if [ -z $VALIDROOT ]; then
  source ./validation_setup.sh
fi

if [ "$DO_ALL" == "yes" ]; then
  DO_HADRO="yes"
  DO_SAMPS="yes"
  DO_SPLCH="yes"
  DO_EVSMP="yes"
  DO_EXDTA="yes"
  DO_SFCMP="yes"
fi


if [ "$DO_HADRO" == "yes" ]; then
  do_gvld_hadronz_test
fi

if [ "$DO_SAMPS" == "yes" ]; then
  do_gvld_sample_scan
fi

if [ "$DO_SPLCH" == "yes" ]; then
  do_gvld_xsec_comp
fi

if [ "$DO_EVSMP" == "yes" ]; then
  do_gvld_sample_comp
fi

if [ "$DO_EXDTA" == "yes" ]; then
  do_gvld_nu_xsec
fi

if [ "$DO_SFCMP" == "yes" ]; then
  do_gvld_sf
fi

if [ -e "reports.tgz" ]; then
  rm reports.tgz
fi

cp run_validation.sh reports
cp analyze_sample_scan.py reports
tar -cvzf reports.tgz reports
