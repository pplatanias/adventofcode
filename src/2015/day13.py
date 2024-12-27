from collections import defaultdict
from itertools import combinations, permutations


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
    "Finds the largest hamiltonian cycle, aka returns to start, does not give the path"

    start = nodes[0]
    nodes = nodes[1:]
    for node in nodes:
        karpdick[((node,), node)] = edges[(start, node)]

    for i in range(2, len(nodes) + 1):
        for route in combinations(nodes, i):
            dists = []
            for k in route:
                dists = []
                for m in route:
                    if m != k:
                        dists.append(karpdick[(tuple(sorted(tuple(set(route) - set([k])))), m)] + edges[(m, k)])
                karpdick[(tuple(sorted(route)), k)] = max(dists)

    dists = []
    for k in nodes:
        dists.append(karpdick[(tuple(sorted((nodes))), k)] + edges[(k, start)])

    return max(dists)


# Part 1
nodes, edges = get_input('inputs/2015/day13.txt')
karpdick = {}
print(heldkarp_cycle(tuple(nodes)))

# Part 2
nodes, edges = get_input('inputs/2015/day13b.txt')
karpdick = {}
print(heldkarp_cycle(tuple(nodes)))
