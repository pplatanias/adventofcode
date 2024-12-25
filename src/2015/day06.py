import re

import numpy as np

with open('inputs/2015/day6.txt', 'r') as file:
    rows = file.read().replace('toggle', '2').replace('turn on', '1').replace('turn off', '0')
    rows = re.findall(r'(\d) (\d*),(\d*) through (\d*),(\d*)', rows)
    rows = [[int(elem) for elem in row] for row in rows]

# Part 1
leny = 1000
lenx = 1000
ledmap = np.zeros(shape=(lenx, leny))

for cmd, x, y, maxx, maxy in rows:
    if cmd == 0:
        ledmap[x:maxx + 1, y:maxy + 1] = 0
    elif cmd == 1:
        ledmap[x:maxx + 1, y:maxy + 1] = 1
    elif cmd == 2:
        ledmap[x:maxx + 1, y:maxy + 1] = 1 - ledmap[x:maxx + 1, y:maxy + 1]
print(np.count_nonzero(ledmap))

# Part 2
leny = 1000
lenx = 1000
ledmap = np.zeros(shape=(lenx, leny))

for cmd, x, y, maxx, maxy in rows:
    if cmd == 0:
        ledmap[x:maxx + 1, y:maxy + 1] = np.maximum(ledmap[x:maxx + 1, y:maxy + 1] - 1, 0)
    elif cmd == 1:
        ledmap[x:maxx + 1, y:maxy + 1] += 1
    elif cmd == 2:
        ledmap[x:maxx + 1, y:maxy + 1] += 2
print(sum(sum(ledmap)))
