#!/bin/sh

# filelist='gntp.804.ghep.root gntp.591.ghep.root gntp.591.gtrac.root gntp.591.gst.root gntp.804.gtrac.root gntp.804.gst.root'
filelist='
gntp.804.ghep.root
gntp.591.ghep.root
gntp.591.gtrac.root
gntp.591.gst.root
gntp.804.gtrac.root
gntp.804.gst.root
'
path=/minerva/app/users/perdue/GENIE/runs
user=perdue
machine=minervagpvm02.fnal.gov

for filenam in $filelist
do
  scp ${user}@${machine}:${path}/${filenam} .
done
