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


### Naive solutions
import random
from typing import Callable, Union, List, Tuple

import numpy as np
from numpy import asarray
from numpy import exp
from numpy import array
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed

i_,f_,l_,L_,r_,M_,m_,x_,e_,a_,s_,S_,z_,rl_=int,float,len,list,range,max,min,map,enumerate,abs,sum,set,zip,lambda _:r_(l_(_))
lmi_ = lambda _:list(map(int, _))

# Naive looping solution
# 483 characters, 14 line breaks
def day7_part1_loop(objective: Callable, raw: List[int]) -> Tuple[int, int]:
    """
    Naive solution
    Loop over every possibility and track the lowest found
    :param raw:
    :return:
    """
    global fi
    fi = list(map(int, raw.split(',')))
    best, best_eval = 0, objective(0)
    for each in range(0, max(fi)+1):
        curr, curr_eval = each, objective(each)
        if curr_eval < best_eval:
            best, best_eval = curr, curr_eval
    return best, best_eval
# Golfed loop approach
# 226 characters, 7 line breaks
def d70l(r,f=0):
 r=lmi_(r.split(','))
 o=((lambda p:s_([a_(e-p)for e in r])),(lambda p:s_([(f_(a_(p-e))**2+f_(a_(p-e)))/2for e in r])))[f]
 b,B=0,o(0)
 for _ in r_(0,M_(r)+1):
  c,C=_,o(_)
  if C<B:b,B=c,C
 return B


# Numpy approach
from scipy.optimize import minimize_scalar
def parse_data():
    with open('input.txt') as f:
        data = f.read()
    return np.loadtxt([data], delimiter=",", dtype=int)
def part_one(data):
    return minimize_scalar(lambda x: np.abs(round(x) - data).sum()).fun
def part_two(data):
    return minimize_scalar(lambda x: (np.abs(round(x) - data) * (np.abs(round(x) - data) + 1) // 2).sum()).fun
if __name__ == '__main__':
    data = parse_data()
    print(f'Day 07 Part 01: {part_one(data)}')
    print(f'Day 07 Part 02: {part_two(data)}')
# Golfed Numpy approach
# 224 characters, 5 line breaks
from scipy.optimize import minimize_scalar as MS
R_=round
def p():
 with open('input.txt')as f:r=f.read()
 return np.loadtxt([r],delimiter=",",dtype=i_)
def d70n():
 return MS(lambda x:np.abs(R_(x)-p()).sum()).fun,MS(lambda x:(np.abs(R_(x)-p())*(np.abs(R_(x)-p())+1)//2).sum()).fun


# Naive Annealing Situation
# 2235 chracters, 75 line breaks
def objective_part1(pos: int) -> Union[int, float]:
    """
    Evaluation function to determine cost for given position
    :param pos:
    :return:
    """
    cost = 0
    for each in fi:
        cost += abs(each - pos)
    return cost


def objective_part2(pos: int) -> Union[int, float]:
    cost = 0
    for each in fi:
        distance = float(abs(each - pos))
        triangle_num = (distance ** 2 + distance) / 2
        cost += triangle_num
    return int(cost)


def simulated_annealing(
        objective: Callable,
        bounds: array,
        n_iterations: int,
        step_size: Union[int, float],
        temp: Union[int, float]
    ) -> Tuple[float, float]:
    """
    Simulated annealing aka Gradient descent w/ randomness

    :param objective:
    :param bounds:
    :param n_iterations:
    :param step_size:
    :param temp:
    :return:
    """
    # generate & evaluate an initial point
    best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    best_eval = objective(best)
    curr, curr_eval = best, best_eval
    for i in range(n_iterations):
        # take a step and evaluate
        candidate = curr + randn(len(bounds)) * step_size
        candidate_eval = objective(candidate)
        if candidate_eval < best_eval:
            best, best_eval = candidate, candidate_eval
            print('>%d f(%s) = %.5f' % (i, best, best_eval))
        # metropolis acceptance criteria allows to randomly use
        # 'worse' candidates to escape local basins
        diff = candidate_eval - curr_eval
        t = temp / float(i + 1)
        metropolis = exp(-diff / t)
        if diff < 0 or rand() < metropolis:
            curr, curr_eval = candidate, candidate_eval
    return (best, best_eval)


def day7_part1_anneal(raw):
    """
    Simulated annealing approach
    :param raw:
    :return:
    """
    global fi
    fi = list(map(int, raw.split(',')))
    seed(1)
    bounds = asarray([[0, max(fi)]])
    n_iterations = 1000
    step_size = 0.1 * random.randint(1, 1000)
    temp = 1 * random.randint(1, 1000)
    best, score = simulated_annealing(objective_part1, bounds, n_iterations, step_size, temp)
    print('Done!')
    print('f(%s) = %f' % (best, score))
    return best, score
# Golfed simulated annealing approach
# 341 characters, 14 line breaks
from numpy import asarray as A
from numpy import exp as E
from numpy.random import randn as N
from numpy.random import rand as R
from numpy.random import seed as S
# f=0 for part 1, f=1 for part 2
def d70(r,s=0.1,T=1,f=1):
 S(1)
 r=lmi_(r.split(','))
 o=((lambda p:s_([a_(e-p)for e in r])),(lambda p:s_([(f_(a_(p-e))**2+f_(a_(p-e)))/2for e in r])))[f]
 b=A([[0,M_(r)]])
 z=b[:,0]+R(l_(b))*(b[:,1]-b[:,0])
 Z=o(z)
 x,X=z,Z
 for i in r_(1999):
  y=x+N(l_(b))*s
  Y=o(y)
  if Y<Z:z,Z=y,Y
  if Y-X<0|(N()<E(-Y-X/(T/(i+1.)))):x,X=y,Y
 return Z


if __name__ == '__main__':
    print(globals()['d' + input('> ')](input('>> ')))  # ENTER to EOF
    # print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
    # print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
    # print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
