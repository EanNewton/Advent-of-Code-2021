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
i_,l_,r_,M_,m_,rl_=int,len,range,max,min,lambda _:r_(l_(_))

### Naive solutions
# 2681 characters, 67 line breaks
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
    boards_copy = copy.deepcopy(rows)
    winner = None
    for called_number in calls:
        last_call = called_number
        print("Call: {}".format(called_number))
        print("Boards: {}".format(boards))
        for board_idx, board in enumerate(rows):
            print("Current Board {}: {}".format(board_idx, board))
            for row_idx, row in enumerate(board):
                print("Current Row {}: {}".format(row_idx, row))
                if called_number in row:
                    print("Popping {} from {} at idx {}".format(called_number, row, row.index(called_number)))
                    row.pop(row.index(called_number))
                if len(row) == 0:
                    print("Length of Board {} Row {} is 0.".format(board_idx, row_idx))
                    winner = boards_copy[board_idx]
                    return calculate_score(winner, calls, last_call)
        for board_idx, board in enumerate(columns):
            for col_idx, col in enumerate(board):
                if called_number in col:
                    col.pop(col.index(called_number))
                if len(col) == 0:
                    winner = boards_copy[board_idx]
                    return calculate_score(winner, calls, last_call)
    return None


### Golfed Solutions
# 595 characters, 14 line breaks
# 22.19% of Naive
def d41(r):
 def _t(b,c,r,n):
  for h_,h in enumerate(r):
   for _ in h:
    if n in _:_.pop(_.index(n))
    if l_(_)==0:
     c=[i_(_)for _ in c]
     return i_(n)*sum([_ for _ in[x for y in[list(map(i_,_))for _ in b[h_]]for x in y]if _ not in c[0:c.index(i_(n))+1]])
 c=[r.splitlines()][0][0].split(',')
 b=[x.split()for x in[_ for _ in r.splitlines()[1::]if _]]
 rc=[[b[n:n+5]for n in r_(0,l_(b),5)]]
 rc.extend([[[[j[e]for j in r]for e in rl_(r[0])]for _ in rc[0]],dc(rc[0])])
 for i in c:
  t=[_t(rc[2],c,rc[k],i)for k in(0,1)]
  if not all([_==None for _ in t]):return next(filter(None,t))

if __name__ == '__main__':
    # print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
    # print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
    print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
