import copy


def traverse(map, y, x, steps=0, speculate=True):
    global loop_cnt
    while True:
        try:
            steps += 1
            dy, dx = DT[map[y][x]]
            next_y = y + dy
            next_x = x + dx
            if next_y < 0 or next_x < 0:
                raise IndexError

            next = map[next_y][next_x]

            if next != '#' and next != 'O':

                if speculate:
                    if next == '.':
                        speculate_map = copy.deepcopy(map)
                        speculate_map[y + dy][x + dx] = 'O'
                        speculate_y = y
                        speculate_x = x

                        isloop = traverse(speculate_map, speculate_y, speculate_x, steps=0, speculate=False)
                        if isloop:
                            loop_cnt += 1

                map[next_y][next_x] = map[y][x]
                y = next_y
                x = next_x

            else:
                dirs = list(DT.keys())
                curr_dir = map[y][x]
                curr_dir_idx = dirs.index(curr_dir)
                map[y][x] = dirs[(curr_dir_idx + 1) % len(dirs)]

            if steps > 40000:
                return 1  # loop
        except IndexError:
            return 0  # non loop


with open('inputs/2024/day6.txt', 'r') as file:
    map = [list(row) for row in file.read().split('\n')]

for yy, rows in enumerate(map):
    for xx, char in enumerate(rows):
        if char != '.' and char != '#':
            y = yy
            x = xx

DT = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

cnt = 0
traverse(map, y, x, steps=0, speculate=False)
for rows in map:
    for ch in rows:
        if ch != '#' and ch != '.':
            cnt += 1
print(cnt)

with open('inputs/2024/day6.txt', 'r') as file:
    map = [list(row) for row in file.read().split('\n')]

loop_cnt = 0
traverse(map, y, x, steps=0, speculate=True)
print(loop_cnt)
