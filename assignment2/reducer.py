#!/usr/bin/python

import sys
num = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    path, other = data_mapped
    if '/assets/js/the-associates.js' in path:
     num = num + 1
print num
