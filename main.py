#!/usr/bin/env python3
"""
Advent of Code 2021
Done in Python3 with goal of playing code golf i.e. low line count
This is not meant to be "good" code, it is dumb, but it is fun
"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"

from cutil import debug, multi_in, map_to_int_list, timer


def d11(r):
    return len([x for x,y in zip(r,r[1:])if x<y])
def d12(r):
    return len([x for x,y in zip([sum(r[i:i+3])for i in range(len(r))if i<len(r)-2],[sum(r[i:i+3])for i in range(len(r))if i<len(r)-2][1:])if x<y])
def d21(r,m=[[0,0]]):
    for o,v in[(o,int(v))for _ in r for(o,v)in[_.split()]]:
        m=[[m[i][j]+{'forward':[[v,0]],'up':[[0,v*-1]],'down':[[0,v]]}.get(o,None)[i][j]for j in range(len(m[0]))]for i in range(len(m))]
    return m[0][0]*m[0][1]
def d22(a,b=[[0,0,0]]):
    for d,e in[(d,int(e))for _ in a for(d,e)in[_.split()]]:
        b=[[b[i][j]+{'forward':[[e,e*b[0][2],0]],'up':[[0,0,e*-1]],'down':[[0,0,e]]}.get(d,None)[i][j]for j in range(len(b[0]))]for i in range(len(b))]
    return b[0][0]*b[0][1]
def d31(r):
    return(lambda _: _[0]*_[1])([int(''.join([f(set(e),key=e.count)for e in[([_[e]for _ in r])for e in range(len(r[0]))]]),2)for f in(min,max)])

if __name__ == '__main__':
    print(globals()['d'+input('>')](multi_in()))
