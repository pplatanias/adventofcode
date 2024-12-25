with open('inputs/2015/day3.txt') as file:
    raw = file.read()

start = (0, 0)
current = (0, 0)
visited = []
dirmap = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
for step in raw:
    next_step = (current[0] + dirmap[step][0], current[1] + dirmap[step][1])
    visited.append(next_step)
    current = next_step
print(len(set(visited)))

start = (0, 0)
current = (0, 0)
visited = []

for step in raw[0::2]:
    next_step = (current[0] + dirmap[step][0], current[1] + dirmap[step][1])
    visited.append(next_step)
    current = next_step

current = (0, 0)
for step in raw[1::2]:
    next_step = (current[0] + dirmap[step][0], current[1] + dirmap[step][1])
    visited.append(next_step)
    current = next_step
print(len(set(visited)))
