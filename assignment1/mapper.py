#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data)> 1:
        ip = str(data[0])
        print "{0}\t{1}".format(ip, 1)
