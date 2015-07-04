#! /usr/bin/python3

import itertools
import sys
import math
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator

if len(sys.argv) != 2 :
    print( sys.argv[0] +  " file ")
    sys.exit(0)

lines = map(lambda x : x.strip(),  open(sys.argv[1], "r").readlines())

lens = {}
for line in lines :
    thelen = len(line)
    lens[thelen] = lens.get(thelen,0)  + 1

nw2len2comb = {}
nw2len2comb[1] = {}
for (k,v) in lens.items():
        nw2len2comb[1][k] = v

def addWord(resMap, inputMap):
    prevNW = max(resMap.keys())
    nw = prevNW + 1 
    nw2len2comb[ nw ] =  {}

    for (k_b, v_b) in resMap[prevNW].items():
        for (k_i,v_i) in inputMap.items():
            newLen = k_b + k_i
            resMap[nw][newLen] = resMap[nw].get(newLen,0) + v_b * v_i

maxwords = 10
for i in range(1,maxwords):
    addWord(nw2len2comb, lens)

nw2len2bits = {} 
for (nw,len2comb) in nw2len2comb.items():
    nw2len2bits[nw] = {}
    for k,v in len2comb.items(): 
        for i in filter(lambda x : x  <= k, len2comb.keys()):
            nw2len2bits[nw][k]  = nw2len2bits[nw].get(k,0) + len2comb[i]


for k in nw2len2bits.keys(): 
    for l in nw2len2bits[k].keys():
        print( "%d\t%d\t%.2f\t%s" %  (k,l,math.log(nw2len2bits[k][l],2),sys.argv[1]) )
