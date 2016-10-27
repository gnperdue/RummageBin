#!/bin/bash

file_le=/pnfs/minerva/persistent/users/perdue/Titan/vertex_dann/titan/lustre/atlas/proj-shared/hep105/sohini/vertex/snapshots/50_LE_DANN_2016-09-20T16.08.00.098418_iter_10700000.caffemodel
file_data=/pnfs/minerva/persistent/users/perdue/Titan/vertex_dann/titan/lustre/atlas/proj-shared/hep105/sohini/vertex/snapshots/50_dataDANN_2016-09-13T21.21.48.709808_iter_10700000.caffemodel
file_no=/pnfs/minerva/persistent/users/perdue/Titan/vertex_dann/titan/lustre/atlas/proj-shared/hep105/sohini/vertex/snapshots/50_noDANN_2016-09-10T10.05.03.739066_iter_10700000.caffemodel

scp perdue@minervagpvm01.fnal.gov:${file_le} .
scp perdue@minervagpvm01.fnal.gov:${file_data} .
scp perdue@minervagpvm01.fnal.gov:${file_no} .

#  get filenames and extensions...
# filename=$(basename "$fullfile")
# extension="${filename##*.}"
# filename="${filename%.*}"

cp $(basename ${file_le}) /Users/perdue/Documents/AI/DANN_Caffe
cp $(basename ${file_data}) /Users/perdue/Documents/AI/DANN_Caffe
cp $(basename ${file_no}) /Users/perdue/Documents/AI/DANN_Caffe
