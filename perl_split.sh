#!/bin/bash

LEARNNAME="skim_data_learn_target0.dat"
TESTNAME="skim_data_test_target0.dat"

NLEARN=`wc -l $LEARNNAME | perl -ne '@l=split /\s+/,$_; print @l[0];'`
echo $NLEARN

NTEST=`wc -l $TESTNAME | perl -ne '@l=split /\s+/,$_; print @l[0];'`
echo $NTEST
