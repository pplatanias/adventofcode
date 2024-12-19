import re
from math import ceil, floor

dim = (103, 101)
time = 100


def get_robots(x):
    robots = []
    exp = re.compile(r'p=(.*),(.*) v=(.*),(.*)')
    for row in x.split('\n'):
        r = re.findall(exp, row)
        x1, x2, x3, x4 = r[0]
        robots.append(((int(x2), int(x1), int(x4), int(x3))))

    return robots


def get_future(robvec, t, dim):
    newy = (robvec[0] + robvec[2] * t) % dim[0]
    newx = (robvec[1] + robvec[3] * t) % dim[1]

    return (newy, newx, robvec[2], robvec[3])


def debug_print(robcoords, dim):
    map = []
    coords = [x[0:2] for x in robcoords]

    for y in range(dim[0]):
        map.append([])
        for x in range(dim[1]):
            if (y, x) in coords:
                map[y].append('X')
            else:
                map[y].append('.')

    for row in map:
        print(''.join(row))


def score(robcoords, dim):
    from math import prod
    qtl = (0, floor(dim[0] / 2), 0, floor(dim[1] / 2))
    qbl = (ceil(dim[0] / 2), dim[0], 0, floor(dim[1] / 2))
    qtr = (0, floor(dim[0] / 2), ceil(dim[1] / 2), dim[1])
    qbr = (ceil(dim[0] / 2), dim[0], ceil(dim[1] / 2), dim[1])
    qs = [qtl, qbl, qtr, qbr]

    sums = []
    for q in qs:
        q_sum = 0
        for coord in robcoords:
            if coord[0] >= q[0] and coord[0] < q[1] and coord[1] >= q[2] and coord[1] < q[3]:
                q_sum += 1
        sums.append(q_sum)

    return prod(sums)


def find_connectivity(robcoords, diag=False):

    conn = 0
    coord_only = set([x[0:2] for x in robcoords])

    for coord in coord_only:
        idy, idx = coord
        direcs = []
        direcs.append((idy - 1, idx))
        direcs.append((idy + 1, idx))
        direcs.append((idy, idx + 1))
        direcs.append((idy, idx - 1))
        if diag:
            direcs.append((idy - 1, idx - 1))
            direcs.append((idy + 1, idx + 1))
            direcs.append((idy - 1, idx + 1))
            direcs.append((idy + 1, idx - 1))

        for direc in direcs:
            if direc in coord_only:
                conn += 1

    return conn


with open('inputs/2024/day14.txt', 'r') as file:
    vec = file.read()

# Part 1
robvecs = get_robots(vec)
robcoords = []
for robvec in robvecs:
    coord = get_future(robvec, time, dim)
    robcoords.append(coord)

print(score(robcoords, dim))

# Part 2
robvecs = sorted(get_robots(vec))
connectivities = []
for i in range(dim[0] * dim[1]):
    robcoords = []
    for robvec in robvecs:
        coord = get_future(robvec, i, dim)
        robcoords.append(coord)
    conn = find_connectivity(robcoords, diag=True)
    connectivities.append([conn, i])

sorted_con = sorted(connectivities, reverse=True)
print(sorted_con[0][1])
