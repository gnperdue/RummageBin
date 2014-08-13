#!/bin/sh

filelist='myfile1.txt myfile2.txt'

for filename in $filelist
do
  echo $filename >> passwds.txt
  echo "-------------" >> passwds.txt
  echo `more $filename` >> passwds.txt
  echo "-------------" >> passwds.txt
done
