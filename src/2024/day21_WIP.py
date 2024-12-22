import heapq
from collections import defaultdict
from functools import cache
from itertools import pairwise, product

keypad_nodes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
keypad_edges = {
    '0': [('2', '^'), ('A', '>')],
    'A': [('3', '^'), ('0', '<')],
    '1': [('4', '^'), ('2', '>')],
    '2': [('5', '^'), ('3', '>'), ('1', '<'), ('0', 'v')],
    '3': [('6', '^'), ('2', '<'), ('A', 'v')],
    '4': [('7', '^'), ('5', '>'), ('1', 'v')],
    '5': [('8', '^'), ('6', '>'), ('4', '<'), ('2', 'v')],
    '6': [('9', '^'), ('5', '<'), ('3', 'v')],
    '7': [('8', '>'), ('4', 'v')],
    '8': [('9', '>'), ('7', '<'), ('5', 'v')],
    '9': [('8', '<'), ('6', 'v')],
}

arrows_nodes = ['<', '^', '>', 'v', 'A']
arrows_edges = {
    'A': [('>', 'v'), ('^', '<')],
    '^': [('v', 'v'), ('A', '>')],
    '>': [('A', '^'), ('v', '<')],
    'v': [('>', '>'), ('<', '<'), ('^', '^')],
    '<': [('v', '>')]
}


@cache
def dijkstras_heap(source, target, keypad=False):
    if keypad:
        nodes = keypad_nodes
        edges = keypad_edges
    else:
        nodes = arrows_edges
        edges = arrows_edges

    dist = defaultdict(lambda: 100000000)
    prev = {}
    dist[source] = 0
    queue = [(0, source)]
    path = []
    for coord in nodes:
        if coord != source:
            prev[coord] = None
            heapq.heappush(queue, (dist[coord], coord))

    weights = {
        '^': 0.01,
        'v': 0.05,
        '>': 0.01,
        '<': 0.05,
    }

    while queue:
        _, u = heapq.heappop(queue)
        for v in edges[u]:
            v_node = v[0]
            v_arrow = v[1]
            alt = dist[u] + 1 + weights[v_arrow]
            if alt < dist[v_node]:
                dist[v_node] = alt
                prev[v_node] = (u, v_arrow)
                heapq.heappush(queue, (dist[v_node], v_node))

            if v_node == target:
                x = v_node
                while prev.get(x):
                    path.insert(0, prev[x][1])
                    x = prev[x][0]

                return dist, prev, path


@cache
def dijkstras_heap_allpaths(source, keypad=False):
    if keypad:
        edges = keypad_edges
    else:
        edges = arrows_edges

    dist = defaultdict(lambda: 100000000)
    dist[source] = 0
    queue = [(0, source)]
    prev = defaultdict(list)

    while queue:
        _, uu = heapq.heappop(queue)

        for v in edges[uu]:
            v_node = v[0]
            v_arrow = v[1]
            alt = dist[uu] + 1
            if alt < dist[v_node]:
                dist[v_node] = alt

                prev[v_node] = [(uu, v_arrow)]
                heapq.heappush(queue, (dist[v_node], v_node))

            elif alt == dist[v_node]:
                prev[v_node].append((uu, v_arrow))
    return dist, prev


@cache
def solver(code, depth):
    for i in range(depth):
        if code[0].isnumeric():
            keypad = True
        else:
            keypad = False

        code = 'A' + code  # Keypad starts on A
        lower_code = ''
        for pair in pairwise(code):
            _, _, path = dijkstras_heap(pair[0], pair[1], keypad=keypad)
            lower_code += (''.join(path))
            lower_code += 'A'
        code = lower_code

    return code


@cache
def recursive_solver(code, depth):
    print('=' * depth, depth, len(code))
    print(dijkstras_heap.cache_info())
    if depth == 0:
        return code
    if code[0].isnumeric():
        keypad = True
    else:
        keypad = False
    code = 'A' + code  # Keypad starts on A
    result = ''

    for pair in pairwise(code):
        _, _, path = dijkstras_heap(pair[0], pair[1], keypad=keypad)
        result += (''.join(path))
        result += 'A'
    return recursive_solver(result, depth - 1)


def recursive_solver_all_paths(code, depth):
    if depth == 0:
        return code
    if code[0].isnumeric():
        keypad = True
    else:
        keypad = False
    code = 'A' + code  # Keypad starts on A
    results = []
    for pair in pairwise(code):
        _, prev = dijkstras_heap_allpaths(pair[0], keypad=keypad)
        paths = build_paths(prev, pair[0], pair[1])
        results.append([''.join(path) + 'A' for path in paths])

    results = [''.join(x) for x in product(*results)]

    return [recursive_solver_all_paths(result, depth - 1) for result in results]


def path_debugger(path, layertype):
    dirs = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    numpad = {
        (0, 0): '7',
        (0, 1): '8',
        (0, 2): '9',
        (1, 0): '4',
        (1, 1): '5',
        (1, 2): '6',
        (2, 0): '1',
        (2, 1): '2',
        (2, 2): '3',
        (3, 1): '0',
        (3, 2): 'A',
    }
    arrows = {
        (0, 1): '^',
        (0, 2): 'A',
        (1, 0): '<',
        (1, 1): 'v',
        (1, 2): '>',
    }
    if layertype == 'arrows':
        mapping = arrows
        start = (0, 2)
    elif layertype == 'numpad':
        mapping = numpad
        start = (3, 2)

    cmds = path.split('A')
    upper_layer = ''
    current = start

    for word in cmds[:-1]:
        for cmd in word:
            next_dir = dirs[cmd]
            next_ = (current[0] + next_dir[0], current[1] + next_dir[1])
            current = next_

        upper_layer += mapping[next_]
    return upper_layer


def build_paths(prev, source, target):

    def backtrack(node):
        if node == source:
            return [[source]]  # Base case: reached the source node
        if node not in prev:
            return []  # No path to the source

        paths = []
        for predecessor, arrow in prev[node]:
            for path in backtrack(predecessor):
                paths.append(path + [arrow])  # Add the current node to each path
        return paths

    return [path[1:] for path in backtrack(target)]


with open('inputs/2024/day21.txt', 'r') as file:
    codes = file.read().split('\n')

s = 0
for code in codes:
    a = set()
    res = recursive_solver_all_paths(code, 3)
    for i in res:
        for j in i:
            minj = min(j, key=lambda x: len(x))
            a.add(minj)
    small = min(a, key=lambda x: len(x))
    print(f'{len(small)} * {int(code[:-1])}')
    s += len(small) * int(code[:-1])
print(s)
print(dijkstras_heap_allpaths.cache_info())

s = 0
for code in codes:
    a = set()
    res = recursive_solver_all_paths(code, 3)
    for i in res:
        for j in i:
            minj = min(j, key=lambda x: len(x))
            a.add(minj)
    small = min(a, key=lambda x: len(x))
    print(small)
    dijkstras_heap.cache_clear()
    res = recursive_solver(small, 23)
    print(res)
    print(f'{len(res)} * {int(code[:-1])}')
    s += len(res) * int(code[:-1])
print(s)
