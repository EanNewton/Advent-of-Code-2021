#!/usr/bin/env python3
"""
Advent of Code 2021
Done in Python3 with goal of playing code golf i.e. low line count
This is not meant to be "good" code, it is dumb, but it is fun
"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"

import sys
from cutil import debug, multi_in
f_,u_,d_='forward','up','down'
i_,l_,r_=int,len,range
rl_=lambda _:r_(l_(_))
def d11(r):
 return l_([x for x,y in zip(r,r[1:])if x<y])
def d12(r):
 return l_([x for x,y in zip([sum(r[i:i+3])for i in rl_(r)if i<l_(r)-2],[sum(r[i:i+3])for i in rl_(r)if i<l_(r)-2][1:])if x<y])
def d21(r,m=[[0,0]]):
 for o,v in[(o,i_(v))for _ in r for(o,v)in[_.split()]]:m=[[m[i][j]+{f_:[[v,0]],u_:[[0,v*-1]],d_:[[0,v]]}.get(o,None)[i][j]for j in rl_(m[0])]for i in rl_(m)]
 return m[0][0]*m[0][1]
def d22(a,b=[[0,0,0]]):
 for d,e in[(d,i_(e))for _ in a for(d,e)in[_.split()]]:b=[[b[i][j]+{f_:[[e,e*b[0][2],0]],u_:[[0,0,e*-1]],d_:[[0,0,e]]}.get(d,None)[i][j]for j in rl_(b[0])]for i in rl_(b)]
 return b[0][0]*b[0][1]
def d31(r):
 return(lambda _:_[0]*_[1])([i_(''.join([f(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]]),2)for f in(min,max)])


def mcb(r: list, pos: int):
 return [max(set(e), key=e.count) for e in [([_[e] for _ in r]) for e in range(len(r[0]))]][pos]

def lcb(r: list, pos: int):
 return [min(set(e), key=e.count) for e in [([_[e] for _ in r]) for e in range(len(r[0]))]][pos]

def d32(r):
 def looper(r,call,pos=0):
  while len(r) > 2:
   r = [_ for _ in r if _[pos] == globals()[call](r, pos)]
   pos += 1
  if globals()[call](r, pos) == globals()[call](r[::-1], pos):
   r = [([r[0],r[1]][r[0][pos]=='1']),([r[1],r[0]][r[0][pos]=='1'])][call=='mcb']
  return int(r, 2)

 return looper(r, 'mcb') * looper(r, 'lcb')

if __name__ == '__main__':
 print(globals()['d' + input('>')](multi_in()))  # Ctrl-D to EOF
 #print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
 #print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
