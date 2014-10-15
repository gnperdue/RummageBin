#!/bin/bash

curl -s 'http://www.iheartquotes.com/api/v1/random?max_lines=2&source=literature'|grep -v "http://iheartquotes"|sed -e 's/&quot;//g'|sed -e 's/--/—/g'
