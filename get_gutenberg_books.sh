#!/usr/bin/env bash

curl -s http://www.gutenberg.org/cache/epub/76/pg76.txt | head -n 10
curl -s http://www.gutenberg.org/cache/epub/77/pg77.txt | head -n 10

curl http://www.gutenberg.org/cache/epub/76/pg76.txt > finn.txt
