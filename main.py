#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"


def multi_in() -> list:
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else: break
    return lines

def day1(raw: list) -> int:
    raw = list(map(int, raw))
    return len([x for x, y in zip(raw, raw[1:]) if x < y])

def day2(raw: list) -> int:
    raw = list(map(int, raw))

    #return len([x for x, y in zip(raw[0:2], raw[1:3]) if x > y])


if __name__ == '__main__':
    print(day2(multi_in()))
