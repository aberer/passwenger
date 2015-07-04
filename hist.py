#! /usr/bin/python

import sys
import math 

if len(sys.argv) != 2 :
    print sys.argv[0] +  " file "
    sys.exit(0)

lines = map(lambda x : x.strip(),  open(sys.argv[1], "r").readlines())

lens = {}
for line in lines :
    thelen = len(line)
    lens[thelen]  = lens.get(thelen,0)  + 1

acc = 0     
for k,v in  lens.items():
    acc += v 
    print "%d\t%d\t%f" % (k,v, math.log(acc,2) )
