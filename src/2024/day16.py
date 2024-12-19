def find_s(m):
    for idy, row in enumerate(m):
        for idx, ch in enumerate(row):
            if ch == 'S':
                return idy, idx


def is_angle(prev, noxt):
    if noxt[0] - prev[0] != 0 and noxt[1] - prev[1] != 0:
        return True


def find_vertices(m):
    vertices = []
    ends = []

    for idy, row in enumerate(m):
        for idx, ch in enumerate(row):
            if ch == '.' or ch == 'E':
                temp_vertices = []
                up = (idy - 1, idx)
                down = (idy + 1, idx)
                right = (idy, idx + 1)
                left = (idy, idx - 1)

                for dir in [up, down, left, right]:
                    if m[dir[0]][dir[1]] == '.':
                        temp_vertices.append(((idy, idx), dir))

                if ch == '.' and len(temp_vertices) >= 3:
                    vertices.extend(temp_vertices)
                elif ch == 'E':
                    vertices.extend(temp_vertices)
                    ends.extend(temp_vertices)

            elif ch == 'S':
                vertices.append(((idy, idx), (idy, idx - 1)))
                start = ((idy, idx), (idy, idx - 1))

    return start, ends, vertices


def get_cardinals(prev, curr, m):
    idy, idx = curr
    prev_y, prev_x = prev

    up = (idy - 1, idx)
    down = (idy + 1, idx)
    right = (idy, idx + 1)
    left = (idy, idx - 1)

    nexts = [x for x in [up, down, right, left] if x != (prev_y, prev_x) and m[x[0]][x[1]] != '#']

    return nexts


def walk(prev, curr, noxt, path, m, vertices, score=0):

    if noxt[0] - prev[0] != 0 and noxt[1] - prev[1] != 0:
        score += 1001
    else:
        score += 1

    if (noxt, curr) in vertices:
        path.append(noxt)
        return (noxt, curr), score, path

    noxts_of_noxt = get_cardinals(curr, noxt, m)
    if len(noxts_of_noxt) == 0:
        return None, 10000000, []
    elif len(noxts_of_noxt) == 1:
        path.append(noxt)
        return walk(curr, noxt, noxts_of_noxt[0], path, m, vertices, score)


def find_neighbors(curr_and_prev, m, vertices):

    curr, prev = curr_and_prev
    nexts = get_cardinals(prev, curr, m)
    neighbors = []
    for noxt in nexts:
        dest, morescore, path = walk(prev, curr, noxt, [curr], m, vertices, score=0)
        if dest:
            neighbors.append((dest, morescore, path))

    return neighbors


def dijkstra(vertices, source):
    dists = {}
    prevs = {}
    queue = []

    for v in vertices:
        dists[v] = 10000000000000
        queue.append(v)

    dists[source] = 0

    while queue:

        u = sorted(queue, key=lambda x: dists[x])[0]
        queue.remove(u)

        neighs = find_neighbors(u, m, vertices)
        for neigh in neighs:
            v = neigh[0]
            alt = dists[u] + neigh[1]
            if alt < dists[v]:
                dists[v] = alt
                prevs[v] = u

    return dists, prevs


def all_dijkstra(vertices, source, edgepaths):
    dists = {}
    prevs = {}
    queue = []

    for v in vertices:
        dists[v] = 10000000000000
        queue.append(v)

    dists[source] = 0

    while queue:

        u = sorted(queue, key=lambda x: dists[x])[0]
        queue.remove(u)

        neighs = find_neighbors(u, m, vertices)
        for neigh in neighs:
            v = neigh[0]
            edgepaths[(u, v)] = neigh[2]

            if v in queue:

                alt = dists[u] + neigh[1]
                if alt < dists[v]:
                    dists[v] = alt
                    prevs[v] = [u]
                elif alt == dists[v]:
                    prevs[v].append(u)

    return dists, prevs


def find_all_paths(prev, source, destination):
    paths = []

    def backtrack(current, path):
        if current == source:
            paths.append([source] + path[::-1])
            return

        for predecessor in prev[current]:
            backtrack(predecessor, path + [current])

    backtrack(destination, [])
    return paths


with open('inputs/2024/day16.txt', 'r') as file:
    m = file.read()

m = [list(x) for x in m.split('\n')]
source, ends, vertices = find_vertices(m)
dists, prevs = dijkstra(vertices, source)

edgepaths = {}
dists, prevs = all_dijkstra(vertices, source, edgepaths)
end = ends[0]

x = find_all_paths(prevs, source, end)

nodes = []
for path in x:
    for pair in zip(path[:-1], path[1:]):
        nodes.extend(edgepaths[pair])

print(dists[end])
print(len(set(nodes)))
