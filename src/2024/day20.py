def find_start(map):
    for idy, row in enumerate(map):
        for idx, ch in enumerate(row):
            if ch == 'S':
                start = (idy, idx)
    return start


def walk(map, source):
    path = [source]
    idy, idx = source

    ch = 'S'
    while ch != 'E':
        up = (idy - 1, idx)
        down = (idy + 1, idx)
        right = (idy, idx + 1)
        left = (idy, idx - 1)
        for v in [up, down, right, left]:
            ch = map[v[0]][v[1]]
            if (ch == '.' or ch == 'E') and v not in path:
                path.append(v)
                idy = v[0]
                idx = v[1]
                break
    return path


def get_shortcuts(min_shortcut, max_cheat_length):
    shortcuts = 0
    for i, start_node in enumerate(path):
        for j, dest_node in enumerate(path[i + 2:]):
            shortcut_length = abs(start_node[0] - dest_node[0]) + abs(start_node[1] - dest_node[1])
            real_steps_between = j + 2
            steps_saved = real_steps_between - shortcut_length

            if shortcut_length <= max_cheat_length and steps_saved >= min_shortcut:
                shortcuts += 1
    return shortcuts


with open('inputs/2024/day20.txt', 'r') as file:
    map = [list(x) for x in file.read().split('\n')]

start = find_start(map)
path = walk(map, start)

print(get_shortcuts(100, 2))
print(get_shortcuts(100, 20))
