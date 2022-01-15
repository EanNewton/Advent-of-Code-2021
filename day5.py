from cutil import multi_in

def filter_input(raw: str) -> list:
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
    for row in board:
        row = [str(_) if _ != 0 else "." for _ in row]
        print(row)


def write_board(board: list) -> None:
    with open("output.txt", "w") as f:
        for row in board:
            row = [str(_) if _ != 0 else "." for _ in row]
            row = ' '.join(row) + "\n"
            f.write(row)
    return None


def score_board(board: list) -> int:
    total = 0
    for row in board:
        for num in row:
            if num > 1:
                total += 1
    return total


def d51(raw: str) -> int:
    """
    At how many points do at least two lines overlap?
    :param raw: user input
    :return: int
    """
    coords, max_ = filter_input(raw)
    board = [[0 for _ in range(max_)] for i in range(max_)]
    for each in coords:
        if each["x1"] == each["x2"]:
            if each["y1"] > each["y2"]:
                each["y1"], each["y2"] = each["y2"], each["y1"]
                each["x1"], each["x2"] = each["x2"], each["x1"]
            for pos in range(each["y1"], each["y2"]+1):
                board[pos][each["x1"]] += 1
        elif each["y1"] == each["y2"]:
            if each["x1"] > each["x2"]:
                each["y1"], each["y2"] = each["y2"], each["y1"]
                each["x1"], each["x2"] = each["x2"], each["x1"]
            for pos in range(each["x1"], each["x2"]+1):
                board[each["y1"]][pos] += 1
    #print_board(board)
    return score_board(board)


if __name__ == '__main__':
    # print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
    # print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
    print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF
