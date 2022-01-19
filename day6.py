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

import numpy as np
import time

from cutil import multi_in, timer

def d61(raw, epoch=256):
    raw = list(map(int, raw[0].split(',')))
    raw = np.array(raw)
    id = np.ones(len(raw))
    times = []
    while epoch:
        start = time.time()
        epoch -= 1
        raw = np.subtract(raw, id)
        for idx, each in enumerate(raw):
            if each < 0:
                raw[idx] = 6
                raw = np.concatenate((raw, [8]))
                id = np.concatenate((id, [1]))
        end = time.time()
        times.append(end-start)
        print(epoch, times[-1], sum(times)/len(times))
    return len(raw)

def d611(raw, epoch=256):
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
        print(epoch, len(raw))
        # print(epoch, times[-1], sum(times)/len(times))
        if epoch < 240:
            print(epoch, times[-1], sum(times[:-10])/10)

    return len(raw)

if __name__ == '__main__':
    print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
    # print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
    # print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
