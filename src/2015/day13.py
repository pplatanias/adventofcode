from collections import defaultdict
from itertools import combinations


def get_input(filename):
    with open(filename, 'r') as file:
        edges = defaultdict(lambda: 0)
        nodes = set()
        for line in file.readlines():
            s, _, sign, amount, _, _, _, _, _, _, e = line.split()
            e = e[:-1]
            if sign == 'lose':
                amount = -int(amount)
            else:
                amount = int(amount)

            edges[(s, e)] += amount
            edges[(e, s)] += amount
            nodes.update([s, e])
    return nodes, edges


def heldkarp_cycle(nodes):
    "Finds the largest hamiltonian cycle but does not return its nodes, just length"

    distances = {}
    start = nodes.pop()

    # Frozensets are used to have unordered, hashable containers of nodes for dict keys.
    nodes = frozenset(nodes)
    for node in nodes:
        distances[(frozenset([
            node,
        ]), node)] = edges[(start, node)]

    for i in range(2, len(nodes) + 1):
        for route in combinations(nodes, i):
            for k in route:
                dists = []
                for m in route:
                    if m != k:
                        previous_shortest = frozenset(set(route) - set([k]))
                        dists.append(distances[((previous_shortest), m)] + edges[(m, k)])
                distances[((frozenset(route)), k)] = max(dists)

    dists = []
    for k in nodes:
        dists.append(distances[((nodes), k)] + edges[(k, start)])

    return max(dists)


# Part 1
nodes, edges = get_input('inputs/2015/day13.txt')
print(heldkarp_cycle(nodes))

# Part 2
nodes, edges = get_input('inputs/2015/day13b.txt')
print(heldkarp_cycle(nodes))
