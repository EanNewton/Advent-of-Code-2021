
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
    :param r:
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


def cmd_move():
    return # ok to call this
def cmd_jump():
    return # ok to call this

if __name__ == '__main__':
     cmd = raw_input('>') # e.g. "move"
     fun = globals()['cmd_' + cmd]
     fun()