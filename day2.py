### Naive solutions
# 1178 characters, 32 line breaks
def day2_part1(raw: list) -> int:
    """
    What do you get if you multiply your final horizontal position by your final depth?
    :param raw: user input
    :return:
    """
    # Identity matrix addition approach
    xy = [[0, 0]]
    for operator, value in [_.split() for _ in raw]:
        identity = {
            'forward': [[int(value), 0]], 
            'up': [[0, int(value) * -1]], 
            'down': [[0, int(value)]]
        }.get(operator, None)
        xy = [[xy[i][j] + identity[i][j] for j in range(len(xy[0]))] for i in range(len(xy))]
    return xy[0][0] * xy[0][1]


def day2_part2(raw: list) -> int:
    """
    What do you get if you multiply your final horizontal position by your final depth?
    :param raw: user input
    :return:
    """
    xya = [[0, 0, 0]]
    for operator, value in [_.split() for _ in raw]:
        identity = {
            'forward': [[int(value), int(value) * xya[0][2], 0]], 
            'up': [[0, 0, int(value) * -1]], 
            'down': [[0, 0, int(value)]]
        }.get(operator, None)
        xya = [[xya[i][j] + identity[i][j] for j in range(len(xya[0]))] for i in range(len(xya))]
    return xya[0][0] * xya[0][1]


### Golfed solutions
# 500 characters, 7 line breaks
# 42.44% of Naive
f_,u_,d_='forward','up','down'
i_,l_,r_,rl_=int,len,range,lambda _:r_(l_(_))
def d21(r,m=[[0,0]]):
 for o,v in[(o,i_(v))for _ in r for(o,v)in[_.split()]]:m=[[m[i][j]+{f_:[[v,0]],u_:[[0,v*-1]],d_:[[0,v]]}.get(o,None)[i][j]for j in rl_(m[0])]for i in rl_(m)]
 return m[0][0]*m[0][1]
def d22(a,b=[[0,0,0]]):
 for d,e in[(d,i_(e))for _ in a for(d,e)in[_.split()]]:b=[[b[i][j]+{f_:[[e,e*b[0][2],0]],u_:[[0,0,e*-1]],d_:[[0,0,e]]}.get(d,None)[i][j]for j in rl_(b[0])]for i in rl_(b)]
 return b[0][0]*b[0][1]