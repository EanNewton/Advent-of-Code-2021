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
i_,l_,r_,M_,m_,e_,rl_=int,len,range,max,min,enumerate,lambda _:r_(l_(_))

def _m(r,i):
 return [M_(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]
def _l(r,i):
 return [m_(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]
def _mr(r):
 return[[_[e]for _ in r]for e in rl_(r[0])]
def _t(b,c,l,s=[]):
    c=[i_(_)for _ in c]
    for _ in[x for y in[list(map(i_,i))for i in b]for x in y]:
        if _ not in c[0:c.index(i_(l))+1]:s.append(_)
    return sum(s)*i_(l)

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
    c=[r.splitlines()][0][0].split(',')
    b=[_ for _ in r.splitlines()[1::]if _]
    b=[x.split()for x in b]
    R=[b[n:n+5]for n in r_(0,l_(b),5)]
    k=dc(R)
    z=[[x,y]for(x, y)in zip([_mr(_)for _ in R],R)]
    for e in c:
        for bi,_ in e_(z):
            for h in _:
                for i in h:
                    if e in i:i.pop(i.index(e))
                    if l_(i)==0:return _t(k[bi],c,e)
def d42(r,W=[]):
    c=[r.splitlines()][0][0].split(',')
    b=[_ for _ in r.splitlines()[1::]if _]
    b=[x.split()for x in b]
    R=[b[n:n+5]for n in r_(0,l_(b),5)]
    k=dc(R)
    z=[[x,y]for(x,y)in zip([_mr(_)for _ in R],R)]
    for e in c:
        for bi,_ in e_(z):
            for h in _:
                for i in h:
                    if e in i:i.pop(i.index(e))
                    if l_(i)==0:
                        if bi not in W:W.append(bi)
                        if l_(W)==l_(z):return _t(k[bi],c,e)


if __name__ == '__main__':
 #print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
 #print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
 print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
