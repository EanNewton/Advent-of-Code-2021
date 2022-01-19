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


from copy import deepcopy as dc
from collections import deque as De
from cutil import debug, multi_in

# cost = 4+len(built_in)
f_,u_,d_='forward','up','down'
i_,l_,L_,r_,M_,m_,x_,e_,a_,s_,S_,z_,rl_=int,len,list,range,max,min,map,enumerate,abs,sum,set,zip,lambda _:r_(l_(_))

# Helper Functions
# most common bit
def _m(r,i):
 return [M_(S_(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]
# least common bit
def _l(r,i):
 return [m_(S_(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]
# matrix rotation
def _mr(r):
 return[[_[e]for _ in r]for e in rl_(r[0])]
# day 4 total score
def _t(b,c,l,s=[]):
    c=[i_(_)for _ in c]
    for _ in[x for y in[L_(x_(i_,i))for i in b]for x in y]:
        if _ not in c[0:c.index(i_(l))+1]:s.append(_)
    return s_(s)*i_(l)
# day 5 filter input
def _f(r,c=[],m=0):
  for _ in [_.split(" -> ")for _ in r.splitlines()]:
    v=[i_(j)for k in _ for j in k.split(',')]
    n={"a":v[0],"c":v[1],"b":v[2],"d":v[3]}
    if m<M_(v):m=M_(v)
    c.append(n)
  return c,m+1
# day 5 score board
def _sb(g):
  return l_([i for s in g for i in s if i>1])
# day 5 draw positions on board
def _sp(p,g,a="c",b="d",c="a",d="b"):
  if p[a]>p[b]:p[a],p[b],p[c],p[d]=p[b],p[a],p[d],p[c]
  for _ in r_(p[a],p[b]+1):
    if a=="c":g[_][p[c]]+=1
    else:g[p[c]][_]+=1
# day 5 Bresenham's line algo
def _L(x,b,c,d,e=0):
 f,g=c-x,d-b
 h,i,j=a_(f)//f,a_(g)//g,a_(g/f)
 for x in r_(x,c,h):
  yield x,b;e+=j
  while e>=.5:b+=i;e-=1
 yield c,d


def d11(r):
 return l_([x for x,y in z_(r,r[1:])if x<y])
def d12(r):
 return l_([x for x,y in z_([s_(r[i:i+3])for i in rl_(r)if i<l_(r)-2],[s_(r[i:i+3])for i in rl_(r)if i<l_(r)-2][1:])if x<y])
def d21(r,m=[[0,0]]):
 for o,v in[(o,i_(v))for _ in r for(o,v)in[_.split()]]:m=[[m[i][j]+{f_:[[v,0]],u_:[[0,v*-1]],d_:[[0,v]]}.get(o,None)[i][j]for j in rl_(m[0])]for i in rl_(m)]
 return m[0][0]*m[0][1]
def d22(a,b=[[0,0,0]]):
 for d,e in[(d,i_(e))for _ in a for(d,e)in[_.split()]]:b=[[b[i][j]+{f_:[[e,e*b[0][2],0]],u_:[[0,0,e*-1]],d_:[[0,0,e]]}.get(d,None)[i][j]for j in rl_(b[0])]for i in rl_(b)]
 return b[0][0]*b[0][1]
def d31(r):
 return(lambda _:_[0]*_[1])([i_(''.join([f(S_(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]]),2)for f in(m_,M_)])
def d32(r):
 def l(r,f,i=0):
  while l_(r)>2:r=[_ for _ in r if _[i]==globals()[f](r,i)];i+=1
  return i_([([r[0],r[1]][r[0][i]=='1']),([r[1],r[0]][r[0][i]=='1'])][f=='_m'],2)
 return l(r,'_m')*l(r,'_l')
def d40(r,W=[],f=0): # f = True for part 1, False for part 2
    c=[r.splitlines()][0][0].split(',')
    b=[_ for _ in r.splitlines()[1::]if _]
    b=[x.split()for x in b]
    R=[b[n:n+5]for n in r_(0,l_(b),5)]
    k=dc(R)
    z=[[x,y]for(x,y)in z_([_mr(_)for _ in R],R)]
    for e in c:
        for bi,_ in e_(z):
            for h in _:
                for i in h:
                    if e in i:i.pop(i.index(e))
                    if l_(i)==0:
                        if f:
                            if bi not in W:W.append(bi)
                            if l_(W)==l_(z):return _t(k[bi],c,e)
                        else:return _t(k[bi],c,e)
def d50(r,f=0): # f = False for part 1, True for part 2
  p,m=_f(r)
  g=[[0 for _ in r_(m)]for i in r_(m)]
  for _ in p:
      if _["a"]==_["b"]:_sp(_,g)
      elif _["c"]==_["d"]:_sp(_,g,"a","b","c","d")
      elif f*a_(_["a"]-_["b"])==a_(_["c"]-_["d"]):
          for x,y in _L(_["a"],_["c"],_["b"],_["d"]):g[y][x]+=1
  return _sb(g)
def d60(r,e=256,c=[0 for _ in r_(0,9)]):
 for _ in L_(x_(i_,r[0].split(','))):c[_]+=1
 for _ in[1]*e:
  c[7]+=c[0]
  d=De(c)
  d.rotate(-1)
  c=L_(d)
 return s_(c)

if __name__ == '__main__':
 #print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
 #print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
 print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
