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

print d[max(d.iteritems(), key=operator.itemgetter(1))[0]]
