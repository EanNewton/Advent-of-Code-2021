#!/usr/bin/env python3
"""
Advent of Code 2021
Done in Python3 with goal of playing code golf i.e. low line/byte count
This is not meant to be "good" code.
It is dumb, it is insecure, it is inefficient, but it is fun.
"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"

import sys
from copy import deepcopy as dc
from cutil import debug, multi_in

f_,u_,d_='forward','up','down'
i_,l_,r_,M_,m_,rl_=int,len,range,max,min,lambda _:r_(l_(_))

def _m(r,i):
 return [M_(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]
def _l(r,i):
 return [m_(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]


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
 return(lambda _:_[0]*_[1])([i_(''.join([f(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]]),2)for f in(m_,M_)])
def d32(r):
 def l(r,f,i=0):
  while l_(r)>2:r=[_ for _ in r if _[i]==globals()[f](r,i)];i+=1
  return i_([([r[0],r[1]][r[0][i]=='1']),([r[1],r[0]][r[0][i]=='1'])][f=='_m'],2)
 return l(r,'_m')*l(r,'_l')
def d41(r):
 def _t(b,c,r,n):
  for h_,h in enumerate(r):
   for _ in h:
    if n in _:_.pop(_.index(n))
    if l_(_)==0:
     c=[i_(_)for _ in c]
     return i_(n)*sum([_ for _ in[x for y in[list(map(i_,_))for _ in b[h_]]for x in y]if _ not in c[0:c.index(i_(n))+1]])
 c=[r.splitlines()][0][0].split(',')
 b=[x.split()for x in[_ for _ in r.splitlines()[1::]if _]]
 rc=[[b[n:n+5]for n in r_(0,l_(b),5)]]
 rc.extend([[[[j[e]for j in r]for e in rl_(r[0])]for _ in rc[0]],dc(rc[0])])
 for i in c:
  t=[_t(rc[2],c,rc[k],i)for k in(0,1)]
  if not all([_==None for _ in t]):return next(filter(None,t))


if __name__ == '__main__':
 #print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
 #print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
 print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
