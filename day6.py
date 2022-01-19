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

from collections import deque as De

import numpy as np
import time

from cutil import multi_in, timer

# Naive solution
# 839 characters, 26 line breaks
def day6_part0(raw: str, epochs=256) -> int:
    """
    # The fastest approach
    # Track how many fish are at each level rather than each fish itself
    # Use deque rotation to both decrement all levels and "append a new fish" in one step
    :param raw:
    :param epochs:
    :return:
    """
    raw = list(map(int, raw[0].split(',')))
    count = [0 for _ in range(0,9)]
    times = []
    for each in raw:
        count[each] += 1
    while epochs:
        start = time.time()
        epochs -= 1
        count[7] += count[0]
        deq = collections.deque(count)
        deq.rotate(-1)
        count = list(deq)
        end = time.time()
        times.append(end-start)
        print("Epoch: {}; Time: {}; Sum: {}; Count: {}".format(
            epochs, times[-1], sum(count), count))
    print(sum(times))
    return sum(count)

# A couple other (notably worse) approaches
# 1283-563=720, 39-13=26
def day6_part0_list(raw: str, epoch=256) -> int:
    """
    Naive approach tracking every individual fish in a list
    Becomes unusably slow as the list exponentially grows

    Slightly faster than numpy
    Epoch | # Fish | Time last epoch | Time avg
    209 399 0.0 0.0
    208 470 0.0 0.0
    207 546 0.0009970664978027344 2.0348295873525193e-05
    206 603 0.0 1.9941329956054688e-05
    205 632 0.0 1.9550323486328125e-05
    ...
    53 777398256 58.654292821884155 3.259695462992626
    52 857008894 61.89703011512756 3.5471333779540717
    ...
    46 1488908416 115.22793412208557 6.062511526970637
    45 1634407150 130.7987356185913 6.653678465793483
    44 1806891705 158.14494943618774 7.368259932634966
    43 2001051167 171.0178678035736 8.136567950808386
    :param raw:
    :param epoch:
    :return:
    """
    raw = list(map(int, raw[0].split(',')))
    times = []
    while epoch:
        start = time.time()
        epoch -= 1
        for idx, each in enumerate(raw):
            if each:
                raw[idx] -= 1
            else:
                raw[idx] = 6
                raw.append(8)
        end = time.time()
        times.append(end-start)
        print(epoch, len(raw), times[-1], sum(times)/len(times))
    print(sum(times))
    return len(raw)


def day6_part0_numpy(raw: str, epoch=256) -> int:
    """
    Alternative implementation using numpy and ones array
    The slowest approach tested
    :param raw:
    :param epoch:
    :return:
    """
    raw = list(map(int, raw[0].split(',')))
    raw = np.array(raw)
    ones = np.ones(len(raw))
    times = []
    while epoch:
        start = time.time()
        epoch -= 1
        raw = np.subtract(raw, ones)
        for idx, each in enumerate(raw):
            if each < 0:
                raw[idx] = 6
                raw = np.concatenate((raw, [8]))
                ones = np.concatenate((ones, [1]))
        end = time.time()
        times.append(end-start)
        print(epoch, len(raw), times[-1], sum(times)/len(times))
    print(sum(times))
    return len(raw)

"""
Golfed solution
163 characters, 7 line breaks, 19.42% of Naive
The fastest approach, sum time for same dataset: 0.0009982585906982422
It completes the entire dataset faster than the other approaches complete a single epoch.
Track how many fish are at each level rather than each fish itself
Use deque rotation to both decrement all levels and "append a new fish" in one step
"""
from collections import deque as De
i_,r_,L_,x_,s_=int,range,list,map,sum
def d60(r,e=256,c=[0 for _ in r_(0,9)]):
 for _ in L_(x_(i_,r[0].split(','))):c[_]+=1
 for _ in[1]*e:
  c[7]+=c[0]
  d=De(c)
  d.rotate(-1)
  c=L_(d)
 return s_(c)

if __name__ == '__main__':
    print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
    # print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
    # print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
