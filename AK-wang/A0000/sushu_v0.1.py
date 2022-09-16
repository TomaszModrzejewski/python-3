#!/bin/env python
#-*-coding:utf-8-*-

import sys
import math 

def prime(n):
    if n%2 == 0:
        return n==2
    if n%3 == 0:
        return n==3
    if n%5 == 0:
        return n==5
    return next((0 for p in xrange(7,int(math.sqrt(n))+1,2) if n%p == 0), 1)  

if __name__ == "__main__":
    n = int(sys.argv[1])
    for i in xrange(2,n+1): #1不是素数,从2开始
        if prime(i):
            print i

#$ time ./sushu_v0.1.py 100000|wc -l
#9592

#real	0m0.287s
#user	0m0.282s
#sys	0m0.009s
