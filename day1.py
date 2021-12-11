### Naive solutions
# 738 characters, 21 line breaks
def day1_part1(raw: list) -> int:
    """
    How many measurements are larger than the previous measurement?
    :param raw: user input
    :return: int
    """
    counter = []
    for x, y in zip(raw, raw[1:]):
        if x < y:
            counter.append(x)
    return len(counter)


def day1_part2(raw: list) -> int:
 """
 Your goal now is to count the number of times the sum of
 measurements in this sliding window increases from the previous sum.
 :param raw: user input
 :return: int
 """
 return len([x for x, y in zip([sum(raw[index:index + 3]) for index in range(len(raw)) if index < len(raw) - 2],
                               [sum(raw[index:index + 3]) for index in range(len(raw)) if index < len(raw) - 2][1:]) if x < y])


### Golfed solutions
# 236 characters, 4 line breaks
# 30.17% of Naive
l_,r_,rl_=len,range,lambda _:r_(l_(_))
def d11(r):
 return l_([x for x,y in zip(r,r[1:])if x<y])
def d12(r):
 return l_([x for x,y in zip([sum(r[i:i+3])for i in rl_(r)if i<l_(r)-2],[sum(r[i:i+3])for i in rl_(r)if i<l_(r)-2][1:])if x<y])