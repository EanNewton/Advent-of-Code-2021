#!/usr/bin/env python3
"""
Advent of Code 2021
Done in Python3 with goal of playing code golf i.e. low line count
"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"

from cutil import debug, multi_in, map_to_int_list


def day1_p1(raw: list) -> int:
    """
    How many measurements are larger than the previous measurement?
    :param raw: list
    :return: int
    """
    return len([x for x, y in zip(raw, raw[1:]) if x < y])


def day1_p2(raw: list) -> int:
    """
    Your goal now is to count the number of times the sum of
    measurements in this sliding window increases from the previous sum.
    :param raw: list
    :return: int
    """
    return len([x for x, y in zip([sum(raw[idx:idx + 3]) for idx in range(len(raw)) if idx < len(raw) - 2], [sum(raw[idx:idx + 3]) for idx in range(len(raw)) if idx < len(raw) - 2][1:]) if x < y])


if __name__ == '__main__':
    print(day1_p2(map_to_int_list(multi_in())))
