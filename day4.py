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

### Naive solutions
# 3474 characters, 89 line breaks
def matrix_rotate(raw: list) -> list:
    """
    Given a square matrix convert rows to columns.
    :param raw: list of lists
    :return: rotated matrix
    """
    rotate = []
    for each in range(len(raw[0])):
        rotate.append([_[each] for _ in raw])
    return rotate


def calculate_score(board: list, calls: list, last_call: int) -> int:
    """
    Given a winning board, what is the score?
    :param board: winning board
    :param calls: all calls made
    :param last_call: the call that resulted in a winning board
    :return: final score
    """
    calls = [int(_) for _ in calls]
    idx_last = calls.index(int(last_call))+1
    calls = calls[0:idx_last]
    board = [list(map(int, _)) for _ in board]
    flat = [x for y in board for x in y]
    sums = []
    for _ in flat:
     if _ not in calls:
      sums.append(_)
    return sum(sums)*int(last_call)


def day4_part1(raw: list) -> int:
    """
    To guarantee victory against the giant squid, figure out which board will win first.
    What will your final score be if you choose that board?
    :param raw: user input
    :return: final score
    """
    calls = [raw.splitlines()][0][0].split(',')
    boards = [_ for _ in raw.splitlines()[1::] if _]
    boards = [x.split() for x in boards]
    group_size = 5
    rows = [boards[n:n + group_size] for n in range(0, len(boards), group_size)]
    columns = [matrix_rotate(_) for _ in rows]
    boards_copy = dc(rows)
    zipped = [[x,y] for (x, y) in zip(columns, rows)]
    for called_number in calls:
        for board_idx, board in enumerate(zipped):
            for rotation in board:
                for row_idx, row in enumerate(rotation):
                    if called_number in row:
                        print("Popping {} from {} at idx {}".format(called_number, row, row.index(called_number)))
                        row.pop(row.index(called_number))
                    if len(row) == 0:
                        print("Length of Board {} Row {} is 0.".format(board_idx, row_idx))
                        winner = boards_copy[board_idx]
                        return calculate_score(winner, calls, called_number)
    return None


def day4_part2(raw: list) -> int:
    """
    To guarantee victory against the giant squid, figure out which board will win first.
    What will your final score be if you choose that board?
    :param raw: user input
    :return: final score
    """
    calls = [raw.splitlines()][0][0].split(',')
    boards = [_ for _ in raw.splitlines()[1::] if _]
    boards = [x.split() for x in boards]
    group_size = 5
    rows = [boards[n:n + group_size] for n in range(0, len(boards), group_size)]
    columns = [matrix_rotate(_) for _ in rows]
    boards_copy = dc(rows)
    zipped = [[x,y] for (x, y) in zip(columns, rows)]
    winning_boards = []
    for called_number in calls:
        for board_idx, board in enumerate(zipped):
            for rotation in board:
                for row_idx, row in enumerate(rotation):
                    if called_number in row:
                        row.pop(row.index(called_number))
                    if len(row) == 0:
                        winner = boards_copy[board_idx]
                        if board_idx not in winning_boards:
                            winning_boards.append(board_idx)
                        if len(winning_boards) == len(zipped):
                            return calculate_score(winner, calls, called_number)
    return None

# Golfed Solutions
# 1252 characters, 35 line breaks
# 36.03% of naive
i_,l_,r_,M_,m_,e_,rl_=int,len,range,max,min,enumerate,lambda _:r_(l_(_))
def _mr(r):
 return[[_[e]for _ in r]for e in rl_(r[0])]
def _t(b,c,l,s=[]):
    c=[i_(_)for _ in c]
    for _ in[x for y in[list(map(i_,i))for i in b]for x in y]:
        if _ not in c[0:c.index(i_(l))+1]:s.append(_)
    return sum(s)*i_(l)
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

def d40(r,W=[],f=0): # f = True for part 1, False for part 2
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
                        if f:
                            if bi not in W:W.append(bi)
                            if l_(W)==l_(z):return _t(k[bi],c,e)
                        else:return _t(k[bi],c,e)



if __name__ == '__main__':
    # print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
    # print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
    print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
