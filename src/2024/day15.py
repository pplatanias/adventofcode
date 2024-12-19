def push(y, x, dir, map):
    ny, nx = get_dest(dir, y, x)

    if map[ny][nx] == '.':
        move(y, x, dir, map)
        return ny, nx
    elif map[ny][nx] == 'O':
        result = push(ny, nx, dir, map)
        if result:
            move(y, x, dir, map)
            return ny, nx
        else:
            return 0
    elif map[ny][nx] == '#':
        return 0


def move(y, x, dir, map):
    ny, nx = get_dest(dir, y, x)
    map[ny][nx] = map[y][x]
    map[y][x] = '.'


def push2(y, x, dir, map, check_only=False):
    ny, nx = get_dest(dir, y, x)
    if map[ny][nx] == '.':
        if check_only is True:
            return True
        else:
            move(y, x, dir, map)
            return ny, nx
    elif map[ny][nx] == '[' and dir in ['^', 'v']:
        if check_only is True:
            result_1 = push2(ny, nx, dir, map, check_only=check_only)
            result_2 = push2(ny, nx + 1, dir, map, check_only=check_only)
            if result_1 and result_2:
                return True
            else:
                return False
        else:
            result_1 = push2(ny, nx, dir, map, check_only=True)
            result_2 = push2(ny, nx + 1, dir, map, check_only=True)
            if result_1 and result_2:
                push2(ny, nx, dir, map, check_only=False)
                push2(ny, nx + 1, dir, map, check_only=False)
                move(y, x, dir, map)
                return ny, nx
            else:
                return False

    elif map[ny][nx] == ']' and dir in ['^', 'v']:
        if check_only is True:
            result_1 = push2(ny, nx, dir, map, check_only=check_only)
            result_2 = push2(ny, nx - 1, dir, map, check_only=check_only)
            if result_1 and result_2:
                return True
            else:
                return False
        else:
            result_1 = push2(ny, nx, dir, map, check_only=True)
            result_2 = push2(ny, nx - 1, dir, map, check_only=True)
            if result_1 and result_2:
                push2(ny, nx, dir, map, check_only=False)
                push2(ny, nx - 1, dir, map, check_only=False)
                move(y, x, dir, map)
                return ny, nx
            else:
                return 0
    elif map[ny][nx] in [']', '[']:
        if check_only is True:
            result = push2(ny, nx, dir, map, check_only=check_only)
            if result:
                return True
        else:
            result = push2(ny, nx, dir, map, check_only=check_only)
            if result:
                move(y, x, dir, map)
                return ny, nx
            else:
                return 0

    elif map[ny][nx] == '#':
        return 0


def move2(y, x, dir, map):
    ny, nx = get_dest(dir, y, x)
    map[ny][nx] = map[y][x]
    map[y][x] = '.'


def get_dest(dir, y, x):
    dirs = {
        '^': (y - 1, x),
        'v': (y + 1, x),
        '>': (y, x + 1),
        '<': (y, x - 1),
    }
    return dirs[dir]


def prep_inp(x):
    x = [list(row) for row in x.split('\n')]
    return x


def find_cursor(map):
    for idy, row in enumerate(map):
        for idx, ch in enumerate(row):
            if ch == '@':
                return idy, idx


def score(map, target):
    score = 0
    for idy, row in enumerate(map):
        for idx, ch in enumerate(row):
            if ch == target:
                score += 100 * idy + idx
    return score


def widen(map):
    newmap = []
    for idy, row in enumerate(map):
        newrow = []
        for idx, ch in enumerate(row):
            if ch == '#':
                newrow.extend('##')
            if ch == 'O':
                newrow.extend('[]')
            if ch == '.':
                newrow.extend('..')
            if ch == '@':
                newrow.extend('@.')
        newmap.append(newrow)
    return newmap


with open('inputs/2024/day15.txt', 'r') as file:
    cmds = file.readline().strip()
    file.readline()
    raw_map = file.read()

# Part 1
map = prep_inp(raw_map)
y, x = find_cursor(map)
for cmd in cmds:
    result = push(y, x, cmd, map)
    if result:
        y = result[0]
        x = result[1]
print(score(map, 'O'))

# Part 2
map = prep_inp(raw_map)
map = widen(map)
y, x = find_cursor(map)
for cmd in cmds:
    result = push2(y, x, cmd, map, check_only=True)
    if result:
        result = push2(y, x, cmd, map, check_only=False)
    else:
        result = y, x

    if result:
        y = result[0]
        x = result[1]

print(score(map, '['))
