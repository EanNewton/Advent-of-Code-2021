
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


def day2_p1(raw: list) -> int:
    """
    What do you get if you multiply your final horizontal position by your final depth?
    :param raw:
    :return:
    """
    xy = [[0, 0]]
    for op, val in [_.split() for _ in raw]:
        id_ = {'forward': [[int(val), 0]], 'up': [[0, int(val) * -1]], 'down': [[0, int(val)]]}.get(op, None)
        xy = [[xy[i][j] + id_[i][j] for j in range(len(xy[0]))] for i in range(len(xy))]
    return xy[0][0] * xy[0][1]



def day2_p2(raw: list, xya: list) -> int:
    """
    What do you get if you multiply your final horizontal position by your final depth?
    :param raw:
    :return:
    """
    for op, val in [_.split() for _ in raw]:
        id_ = {'forward': [[int(val), int(val) * xya[0][2], 0]], 'up': [[0, 0, int(val) * -1]], 'down': [[0, 0, int(val)]]}.get(op, None)
        xya = [[xya[i][j] + id_[i][j] for j in range(len(xya[0]))] for i in range(len(xya))]
    return xya[0][0] * xya[0][1]


def day3_p1(raw: list) -> int:
    """
    What is the power consumption of the submarine?
    :param raw: user input
    :return:
    """
    rotate = []
    mcb = []
    lcb = []
    for each in range(len(raw[0])):
        rotate.append([_[each] for _ in raw])
    for each in rotate:
        mcb.append(max(set(each), key=each.count))
        lcb.append(min(set(each), key=each.count))

    return int(''.join(mcb),2) * int(''.join(lcb),2)

def day3_p1_medium(r):
    return int(''.join([max(set(e),key=e.count)for e in[([_[e]for _ in r])for e in range(len(r[0]))]]),2)*\
           int(''.join([min(set(e),key=e.count)for e in[([_[e]for _ in r])for e in range(len(r[0]))]]),2)

def mcb(r: list, pos: int):
 return [max(set(e), key=e.count) for e in [([_[e] for _ in r]) for e in range(len(r[0]))]][pos]

def lcb(r: list, pos: int):
 return [min(set(e), key=e.count) for e in [([_[e] for _ in r]) for e in range(len(r[0]))]][pos]

def day3_part2(raw: list) -> int:
    """
    What is the life support rating of the submarine?
    :param raw: user input
    :return:
    """
    def filter(raw: list, f: str, pos: int) -> list:
        return [x for x in raw if x[pos] == f]

    def looper(raw_copy: list, call: str) -> int:
        pos = 0
        while len(raw_copy) > 2:
            raw_copy = filter(raw_copy, globals()[call](raw_copy, pos), pos)
            pos += 1
        # Need to fix 'equal bit' counts for final compare
        # min / max default to the first in list
        # https://docs.python.org/3/library/functions.html#min
        if globals()[call](raw_copy, pos) == globals()[call](raw_copy[::-1], pos):
            if call == 'mcb':
                raw_copy = raw_copy[0] if raw_copy[0][pos] == '1' else raw_copy[1]
            else:
                raw_copy = raw_copy[1] if raw_copy[0][pos] == '1' else raw_copy[0]
        return int(raw_copy, 2)

    return looper(raw, 'mcb') * looper(raw, 'lcb')



def cmd_move():
    return # ok to call this
def cmd_jump():
    return # ok to call this

if __name__ == '__main__':
     cmd = raw_input('>') # e.g. "move"
     fun = globals()['cmd_' + cmd]
     fun()




def _t(r,i):
 #broken for max, returns second largest value for some reason
 return(lambda _: _[0])([[f(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i] for f in (min, max)])


def _m(r,i):
 return [max(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]

def _l(r,i):
 return [min(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]

def d32(r):
 def l(r,f,n=0,i=0):
  while l_(r)>2:r=[_ for _ in r if _[i]==globals()[f](r,i,n)];i+=1
  r=[([r[0],r[1]][r[0][i]=='1']),([r[1],r[0]][r[0][i]=='1'])][f=='_m']
  return i_(r,2)
 return l(r,'_t')*l(r,'_t',n=1)

if __name__ == '__main__':
 print(globals()['d' + input('>')](multi_in()))  # Ctrl-D to EOF
 #print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
 #print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF

#f=lambda l,i=0:(z:=lambda:--(len(l)>2),[*((o(l),i)for _ in iter(z,0))])and None
