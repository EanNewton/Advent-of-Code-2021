### Naive solutions
# 2145 characters, 64 line breaks
def day3_part1(raw: list) -> int:
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


# Most Common Bit
def mcb(raw: list, position: int) -> list:
    """
    Find the most common bit from a list.
    :param raw: user input
    :param position:
    :return:
    """
    return [max(set(each), key=each.count) for each in [([_[each] for _ in raw]) for each in range(len(raw[0]))]][position]


# Least Common Bit
def lcb(raw: list, position: int) -> list:
    """
    Find the least common bit from a list.
    :param raw: user input
    :param position:
    :return:
    """
    return [min(set(each), key=each.count) for each in [([_[each] for _ in raw]) for each in range(len(raw[0]))]][position]


def day3_part2(raw: list) -> int:
    """
    What is the life support rating of the submarine?
    :param raw: user input
    :return:
    """
    def filter(raw: list, func_call: str, position: int) -> list:
        return [x for x in raw if x[position] == func_call]

    def looper(raw_copy: list, func_call: str) -> int:
        position= 0
        while len(raw_copy) > 2:
            raw_copy = filter(raw_copy, globals()[func_call](raw_copy, position), position)
            position += 1
        # Need to fix 'equal bit' counts for final compare
        # min / max default to the first in list
        # https://docs.python.org/3/library/functions.html#min
        if globals()[func_call](raw_copy, position) == globals()[func_call](raw_copy[::-1], position):
            if func_call == 'mcb':
                raw_copy = raw_copy[0] if raw_copy[0][position] == '1' else raw_copy[1]
            else:
                raw_copy = raw_copy[1] if raw_copy[0][position] == '1' else raw_copy[0]
        return int(raw_copy, 2)

    return looper(raw, 'mcb') * looper(raw, 'lcb')


### Golfed Solutions
# 596 characters, 11 line breaks
# 27.78% of Naive
i_,l_,r_,M_,m_,rl_=int,len,range,max,min,lambda _:r_(l_(_))
def _m(r,i):
 return [M_(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]
def _l(r,i):
 return [m_(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]][i]
def d31(r):
 return(lambda _:_[0]*_[1])([i_(''.join([f(set(e),key=e.count)for e in[([_[e]for _ in r])for e in rl_(r[0])]]),2)for f in(m_,M_)])
def d32(r):
 def l(r,f,i=0):
  while l_(r)>2:r=[_ for _ in r if _[i]==globals()[f](r,i)];i+=1
  return i_([([r[0],r[1]][r[0][i]=='1']),([r[1],r[0]][r[0][i]=='1'])][f=='_m'],2)
 return l(r,'_m')*l(r,'_l')
