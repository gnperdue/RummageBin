#!/bin/bash

LHAPDFSRC=LHAPDF-6.1.4.tar.gz
GENIEVER=R-2_9_0
BOOSTSRC=boost_1_56_0.tar.gz

# bash `cut`
LHAPDFMAJOR=`echo $LHAPDFSRC | cut -c8-8`
echo $LHAPDFMAJOR

BOOSTVER=`echo $BOOSTSRC | cut -c7-12`
echo $BOOSTVER


# perl
BOOSTVER=`echo $BOOSTSRC | perl -ne '@l=split("_",$_);print @l[2];'`
echo $BOOSTVER

GENIE_MAJOR=`echo $GENIEVER | perl -ne '@l=split("-",$_);@m=split("_",@l[1]);print @m[1];'`
echo $GENIE_MAJOR


# Python - this requires probably at least Python 2.6; it definitely fails on 2.4
BOOSTVER=`echo $BOOSTSRC | python -c "from __future__ import print_function; import sys;t=sys.stdin.readline().split('.')[0].split('_');print('%s.%s.%s'%(t[1],t[2],t[3]))"`
echo $BOOSTVER


