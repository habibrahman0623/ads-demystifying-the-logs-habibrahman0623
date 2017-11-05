#!/usr/bin/python
import operator
import sys
d = dict()
for line in sys.stdin:
    path = line.strip()
    if path in d:
      d[path] +=1
    else: 
      d[path] = 1

print len(d.keys())
