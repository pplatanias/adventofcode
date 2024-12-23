import networkx as nx

with open('inputs/2024/day23.txt') as file:
    edges = [x.split('-') for x in file.read().split('\n')]

G = nx.from_edgelist(edges)

# Part 1
cnt = 0
cliques = nx.enumerate_all_cliques(G)
for triangle in cliques:
    if len(triangle) == 3:
        if any(node.startswith('t') for node in triangle):
            cnt += 1
print(cnt)

# Part 2
cliques = list(nx.enumerate_all_cliques(G))
big = cliques[-1]
print(','.join(sorted(big)))
