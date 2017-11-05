#!/usr/bin/python
import sys
import urlparse

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data)> 1:
        url = data[6]
        path = urlparse.urlparse(url).path
        print str(path)
