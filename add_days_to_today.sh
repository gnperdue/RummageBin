#!/bin/bash
echo $1 | perl -MPOSIX -ne '@now = localtime; $now[3] += $_; print scalar localtime mktime @now; print "\n"'
