#!/usr/bin/python

import sys
num = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    ip, other = data_mapped
    if str(ip) == "10.99.99.186":
     num = num + 1
print num
