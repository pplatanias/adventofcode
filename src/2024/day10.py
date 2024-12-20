def get_map(input):
    return [list(y) for y in input.split('\n')]


def walk(map, idy, idx, max_y, max_x):
    paths = []
    curr = int(map[idy][idx])
    dirs = [
        dir for dir in [[idy + 1, idx], [idy - 1, idx], [idy, idx + 1], [idy, idx - 1]]
        if dir[0] < max_y and dir[0] >= 0 and dir[1] < max_x and dir[1] >= 0
    ]
    for dir in dirs:
        next = map[dir[0]][dir[1]]
        if next != '.':
            next = int(next)
            if next - curr == 1:
                if next < 9:
                    paths.extend(walk(map, dir[0], dir[1], max_y, max_x))
                if next == 9:
                    paths.append((dir[0], dir[1]))
    return paths


def walk2(map, idy, idx, max_y, max_x):
    paths = 0
    curr = int(map[idy][idx])
    dirs = [
        dir for dir in [[idy + 1, idx], [idy - 1, idx], [idy, idx + 1], [idy, idx - 1]]
        if dir[0] < max_y and dir[0] >= 0 and dir[1] < max_x and dir[1] >= 0
    ]
    for dir in dirs:
        next = map[dir[0]][dir[1]]
        if next != '.':
            next = int(next)
            if next - curr == 1:
                if next < 9:
                    paths += walk2(map, dir[0], dir[1], max_y, max_x)
                if next == 9:
                    paths += 1
    return paths


with open('inputs/2024/day10.txt', 'r') as file:
    inp = file.read()

map = get_map(inp)
max_y = len(map)
max_x = len(map[0])

part1 = 0
part2 = 0

for idy, row in enumerate(map):
    for idx, ch in enumerate(row):
        if ch == '0':
            part1 += len(set(walk(map, idy, idx, max_y, max_x)))
            part2 += walk2(map, idy, idx, max_y, max_x)

print(part1)
print(part2)
