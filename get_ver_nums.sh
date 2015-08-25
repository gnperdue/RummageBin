#!/bin/bash

LHAPDFSRC=LHAPDF-6.1.4.tar.gz
LHAPDFMAJOR=`echo $LHAPDFSRC | cut -c8-8`
echo $LHAPDFMAJOR
BOOSTSRC=boost_1_56_0.tar.gz
BOOSTVER=`echo $BOOSTSRC | cut -c7-12`
echo $BOOSTVER
BOOSTVER=`echo $BOOSTSRC | python -c "from __future__ import print_function; import sys;t=sys.stdin.readline().split('.')[0].split('_');print('%s.%s.%s'%(t[1],t[2],t[3]))"`
echo $BOOSTVER

