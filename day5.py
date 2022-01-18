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

# Naive solutions
# 4602 characters, 147 line breaks
# 457.45% of golfed

from typing import Generator

def filter_input(raw: str) -> tuple:
    """
    Convert raw string input to a tuple of:
    (dictionary of cooardinates in x,y pairs, largest value seen)
    :param raw:
    :return:
    """
    lines = [each.split(" -> ") for each in raw.splitlines()]
    coords = []
    max_ = 0
    for line in lines:
        x1, y1 = list(map(int, line[0].split(',')))
        x2, y2 = list(map(int, line[1].split(',')))
        new_line = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
        if max_ < max(new_line.values()):
            max_ = max(new_line.values())
        coords.append(new_line)
    return coords, max_+1


def print_board(board: list) -> None:
    """
    Output board to terminal
    :param board:
    :return:
    """
    for row in board:
        row = [str(_) if _ != 0 else "." for _ in row]
        print(row)


def write_board(board: list) -> None:
    """
    Output board to txt file
    :param board:
    :return:
    """
    with open("output.txt", "w") as f:
        for row in board:
            row = [str(_) if _ != 0 else "." for _ in row]
            row = ' '.join(row) + "\n"
            f.write(row)


def score_board(board: list) -> int:
    """
    Given a board, how many values are 2 or greater?
    :param board:
    :return:
    """
    total = 0
    for row in board:
        for num in row:
            if num > 1:
                total += 1
    return total


def day5_part1(raw: str) -> int:
    """
    At how many points do at least two lines overlap?
    :param raw: user input
    :return: int
    """
    coords, max_ = filter_input(raw)
    board = [[0 for _ in range(max_)] for i in range(max_)]
    for each in coords:
        # Vertical lines
        if each["x1"] == each["x2"]:
            if each["y1"] > each["y2"]:
                # We can only draw from top to bottom in naive solution
                # If the coords indicate the opposite we need to flip
                each["y1"], each["y2"] = each["y2"], each["y1"]
                each["x1"], each["x2"] = each["x2"], each["x1"]
            for pos in range(each["y1"], each["y2"]+1):
                board[pos][each["x1"]] += 1
        # Horizontal lines
        elif each["y1"] == each["y2"]:
            if each["x1"] > each["x2"]:
                # We can only draw from left to right in naive solution
                # If the coords indicate the opposite we need to flip
                each["y1"], each["y2"] = each["y2"], each["y1"]
                each["x1"], each["x2"] = each["x2"], each["x1"]
            for pos in range(each["x1"], each["x2"]+1):
                board[each["y1"]][pos] += 1
    return score_board(board)


def day5_part2(raw: str) -> int:
    """
    At how many points do at least two lines overlap?
    :param raw: user input
    :return: int
    """

    def line(x0: int, y0: int, x1: int, y1: int) -> Generator[int]:
        """
        Bresenham's Line Algorithm, used for diagonals
        :param x0:
        :param y0:
        :param x1:
        :param y1:
        :return:
        """
        deltax = x1 - x0
        dxsign = int(abs(deltax) / deltax)
        deltay = y1 - y0
        dysign = int(abs(deltay) / deltay)
        deltaerr = abs(deltay / deltax)
        error = 0
        y = y0
        for x in range(x0, x1, dxsign):
            yield x, y
            error = error + deltaerr
            while error >= 0.5:
                y += dysign
                error -= 1
        yield x1, y1

    def set_pos(coords, a="y1", b="y2", c="x1", d="x2"):
        if coords[a] > coords[b]:
            # We can only draw from top to bottom in naive solution
            # If the coords indicate the opposite we need to flip
            coords[a], coords[b] = coords[b], coords[a]
            coords[c], coords[d] = coords[d], coords[c]
        for pos in range(coords[a], coords[b] + 1):
            if a == "y1":
                board[pos][coords[c]] += 1
            else:
                board[coords[c]][pos] += 1

    coords, max_ = filter_input(raw)
    board = [[0 for _ in range(max_)] for i in range(max_)]
    for each in coords:
        # Vertical lines
        if each["x1"] == each["x2"]:
            set_pos(each)
        # Horizontal lines
        elif each["y1"] == each["y2"]:
            set_pos(each, "x1", "x2", "y1", "y2")
        # Diagonal Lines
        elif abs(each["x1"] - each["x2"]) == abs(each["y1"] - each["y2"]):
            for x,y in line(each["x1"], each["y1"], each["x2"], each["y2"]):
                board[y][x] += 1
    print_board(board)
    return score_board(board)

# Golfed solutions
# 1006 characters, 34 line breaks
# 21.86% of naive

i_,l_,r_,M_,m_,e_,a_,rl_=int,len,range,max,min,enumerate,abs,lambda _:r_(l_(_))
def _f(r,c=[],m=0):
  for _ in [_.split(" -> ")for _ in r.splitlines()]:
    v=[i_(j)for k in _ for j in k.split(',')]
    n={"a":v[0],"c":v[1],"b":v[2],"d":v[3]}
    if m<M_(v):m=M_(v)
    c.append(n)
  return c,m+1
def _sb(g):
  return l_([i for s in g for i in s if i>1])
def _sp(p,g,a="c",b="d",c="a",d="b"):
  if p[a]>p[b]:p[a],p[b],p[c],p[d]=p[b],p[a],p[d],p[c]
  for _ in r_(p[a],p[b]+1):
    if a=="c":g[_][p[c]]+=1
    else:g[p[c]][_]+=1
def _L(a,b,c,d,e=0):
  z=[c-a,d-b]
  q=a_(z[1]/z[0])
  z=[i_(a_(_)/_)for _ in z]
  for x in r_(a,c,z[0]):
    yield x,b
    e+=q
    while e>=0.5:
      b+=z[1]
      e-=1
  yield c,d
def d50(r,f=0): # f = False for part 1, True for part 2
  p,m=_f(r)
  g=[[0 for _ in r_(m)]for i in r_(m)]
  for _ in p:
      if _["a"]==_["b"]:_sp(_,g)
      elif _["c"]==_["d"]:_sp(_,g,"a","b","c","d")
      elif f*a_(_["a"]-_["b"])==a_(_["c"]-_["d"]):
          for x,y in _L(_["a"],_["c"],_["b"],_["d"]):g[y][x]+=1
  return _sb(g)


if __name__ == '__main__':
    # print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
    # print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
    print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
