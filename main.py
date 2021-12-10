#!/usr/bin/env python3
"""
Advent of Code 2021
Done in Python3 with goal of playing code golf i.e. low line count
This is not meant to be "good" code, it is dumb, but it is fun
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
    return len([x for x, y in zip([sum(raw[i:i + 3]) for i in range(len(raw)) if i < len(raw) - 2], [sum(raw[i:i + 3]) for i in range(len(raw)) if i < len(raw) - 2][1:]) if x < y])


def day2_p1(raw: list, xy: list) -> int:
    """
    What do you get if you multiply your final horizontal position by your final depth?
    :param raw: user input
    :param xy: starting position
    :return:
    """
    for op, val in [_.split() for _ in raw]:
        xy = [[xy[i][j] + {'forward': [[int(val), 0]], 'up': [[0, int(val) * -1]], 'down': [[0, int(val)]]}.get(op, None)[i][j] for j in range(len(xy[0]))] for i in range(len(xy))]
    return xy[0][0] * xy[0][1]


def day2_p2(raw: list) -> int:
    """
    What do you get if you multiply your final horizontal position by your final depth?
    :param raw:
    :return:
    """
    xya = [[0, 0, 0]]
    for op, val in [_.split() for _ in raw]:
        id_ = {'forward': [[int(val), 0]], 'up': [[0, int(val) * -1]], 'down': [[0, int(val)]]}.get(op, None)
        xy = [[xy[i][j] + id_[i][j] for j in range(len(xy[0]))] for i in range(len(xy))]
    return xy[0][0] * xy[0][1]


if __name__ == '__main__':
    print(day2_p1(multi_in(), [[0, 0]]))
