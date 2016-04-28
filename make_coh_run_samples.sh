#!/bin/bash

cp COH_1000060120_splines_BS_rev6122.xml COH_1000060120_splines.xml

energies="
0.5
1.0
1.5"

echo "#Current, energy, run" > coh_run_log.csv

for energy in $energies
do
    run=`echo $energy | perl -lne 'printf "%d", int(10000 + 10 * $_);'`
    ./do_a_run.sh --list COH-CC --target 1000060120 --energy $energy --nus 14 --run $run --seed $run --numevt 50000
    ./do_ghep_conversion.sh $run
    echo "CC, $energy, $run" >> coh_run_log.csv
    run=`echo $energy | perl -lne 'printf "%d", int(20000 + 10 * $_);'`
    ./do_a_run.sh --list COH-NC --target 1000060120 --energy $energy --nus 14 --run $run --seed $run --numevt 50000
    ./do_ghep_conversion.sh $run
    echo "NC, $energy, $run" >> coh_run_log.csv
done
