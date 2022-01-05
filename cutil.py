#!/usr/bin/env python3
"""
Helper functions
"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"

from os import path
import functools
import time


DEFAULT_DIR = path.dirname(path.abspath(__file__))
VERBOSE = 1


def debug(func):
    """Print the function signature and return value"""
    if VERBOSE >= 1:
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            print(f"Calling {func.__name__}({signature})\n")
            value = func(*args, **kwargs)
            print(f"{func.__name__!r} returned {value!r}\n")

            return value

        return wrapper_debug
    else:
        return func


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer


def multi_in() -> list:
    """
    Take input containing line breaks as single input.
    :return: list
    """
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else: break
    return lines


def map_to_int_list(raw: list) -> list:
    """
    Explicitly convert all values in a list to ints.
    :param raw: list
    :return: list
    """
    return list(map(int, raw))


def fetch_file(directory: str, filename: str):
    """Safely read in a dynamically designated local file"""
    with open('{}/docs/{}/{}.txt'.format(DEFAULT_DIR, directory, filename), 'r') as f:
        return f.read()


def wrap(s: str, w: int) -> list:
    """Break a long string s into a list of strings of length w"""
    return [s[i:i + w] for i in range(0, len(s), w)]


def matrix_rotate(raw: list) -> list:
    """Rotate elements in a list of lists by 90 degrees, ie columns -> rows"""
    return [[_[each] for _ in raw] for each in range(len(raw[0]))]
def _mr(r):
 return[[_[e]for _ in r]for e in rl_(r[0])]