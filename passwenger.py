#! /usr/bin/python3

import random
import sys
import argparse
import re

rng = random.SystemRandom()

parser = argparse.ArgumentParser(description='password generator')
parser.add_argument('chars', help="number of characters in password")
parser.add_argument('num', help="number of words to be used")
parser.add_argument('file', help="word list for generating a password")
parser.add_argument('--filter', help="characters to omit")

args = parser.parse_args()

num  = int(args.num)
fn = args.file
lines = list(map(lambda x : x.strip() , open(fn, "r").readlines()))
chars = int(args.chars)

myfilter = ""
if args.filter: 
    myfilter = args.filter 

total = 0
len2words = {}

word2abbrv = {} 
for line in lines:
    abbrv = line 
    if myfilter != "": 
        abbrv = re.sub("[" + myfilter + "]" , '', line)
    word2abbrv[line] = abbrv

for line in lines:
    thelen = len(word2abbrv[line])

    if thelen in len2words:
        len2words[thelen].append(line)
    else :
        len2words[thelen] = list(line)

weights = {}
for (k,v) in len2words.items():
    total += len(v )
    weights[k] = len(v)

    
def determineLen(weights, charsleft, total) :
    left = charsleft
    submap = {}
    reltot = 0 
    for (k,v) in weights.items():
        if k <= left:
            submap[k] = v
            reltot += v 
    
    c = rng.randint(0,reltot)
    res = 0
    for (k,v) in submap.items():
        c -= v
        if c <= 0:
            return k

lens = []
r = list(range(0,num))
r.reverse()
sofar = 0 
for i in r :
    thelen = determineLen(weights,  chars - (sofar + i * 4),total)
    sofar += thelen
    lens.append(thelen)

rng.shuffle(lens)

s = list(map(lambda x : rng.choice(len2words[x]),lens))

if (myfilter  !=  "" ) :
    sMapped = list(map(lambda x : re.sub("[" + myfilter + "]", "", x), s))
else :
    sMapped = list(s )

print(" ".join(s))
print(" ".join(sMapped))
print("".join(map(lambda x : x.title(), sMapped)))
