#! /usr/bin/python3

import sys

if len(sys.argv) != 2:
    print(sys.argv[0] + " file")
    sys.exit(1)


freqs = {} 
total = 0
for line in map(lambda x : x.strip(), open(sys.argv[1],"r").readlines()) :
    for i in line:
        freqs[i] = freqs.get(i,0) + 1
        total += 1 

for k,v in freqs.items():
    print("%s\t%.2f" % (k ,  v / float(total)  * 100 ))
