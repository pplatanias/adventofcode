import heapq
from bisect import bisect_left
from collections import defaultdict


def get_bytes(x):
    import re
    exp = r'(\d*),(\d*)'
    z = re.findall(exp, x)
    return [(int(x[0]), int(x[1])) for x in z]


def get_box(y, x, obstacles):
    coords = []
    for idy in range(y):
        for idx in range(x):
            if (idy, idx) not in obstacles:
                coords.append((idy, idx))
    return coords


def dijkstras_heap(box, source, target):
    dist = defaultdict(lambda: 100000000)
    prev = {}
    dist[source] = 0
    queue = [(0, source)]
    for coord in box:
        if coord != source:
            prev[coord] = None
            heapq.heappush(queue, (dist[coord], coord))

    while queue:
        _, u = heapq.heappop(queue)
        idy, idx = u

        up = (idy - 1, idx)
        down = (idy + 1, idx)
        right = (idy, idx + 1)
        left = (idy, idx - 1)

        for v in [dirr for dirr in [up, down, left, right] if dirr in box and dirr != u]:

            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(queue, (dist[v], v))

        if u == target:
            return dist, prev


def print_box(y, x, box):
    for idy in range(y):
        row = []
        for idx in range(x):
            if (idy, idx) in box:
                row.append('.')
            else:
                row.append('#')
        print(''.join(row))


def helper(i):
    box = get_box(y, x, obstacles[:i])
    dist, _ = dijkstras_heap(box, source, end)
    return dist[end]


with open('inputs/2024/day18.txt', 'r') as file:
    real = file.read()

obstacles = get_bytes(real)
dim = (71, 71)
y, x = dim
source = (0, 0)
end = (70, 70)

box = get_box(y, x, obstacles[:1024])
dist, _ = dijkstras_heap(box, source, end)
print(dist[end])

x = bisect_left(range(len(obstacles)), 5000, key=lambda x: helper(x))
print(obstacles[x - 1])
