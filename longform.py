
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