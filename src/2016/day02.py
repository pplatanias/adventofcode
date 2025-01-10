with open('inputs/2016/day2.txt', 'r') as file:
    rows = file.read().split('\n')

dirmap = {
    'U': (-1, 0),
    'R': (0, 1),
    'L': (0, -1),
    'D': (1, 0),
}
buttonmap = {
    (0, 0): '1',
    (0, 1): '2',
    (0, 2): '3',
    (1, 0): '4',
    (1, 1): '5',
    (1, 2): '6',
    (2, 0): '7',
    (2, 1): '8',
    (2, 2): '9',
}
starmap = {
    (0, 2): '1',
    (1, 1): '2',
    (1, 2): '3',
    (1, 3): '4',
    (2, 0): '5',
    (2, 1): '6',
    (2, 2): '7',
    (2, 3): '8',
    (2, 4): '9',
    (3, 1): 'A',
    (3, 2): 'B',
    (3, 3): 'C',
    (4, 2): 'D',
}


def solve_1():
    buttons = []
    current = [1, 1]
    for row in rows:
        for step in row:
            next_ = [current[0] + dirmap[step][0], current[1] + dirmap[step][1]]
            if all(x >= 0 and x <= 2 for x in next_):
                current = next_
        buttons.append(buttonmap[tuple(current)])
    return buttons


def solve_2():
    buttons = []
    current = [2, 0]
    for row in rows:
        for step in row:
            next_ = [current[0] + dirmap[step][0], current[1] + dirmap[step][1]]
            y = next_[0]
            x = next_[1]
            if y + x >= 2 and y + x <= 6 and abs(y - x) >= 0 and abs(y - x) <= 2 and all(x >= 0 and x <= 4
                                                                                         for x in next_):
                current = next_
        buttons.append(starmap[tuple(current)])
    return buttons


print(''.join(solve_1()))
print(''.join(solve_2()))
