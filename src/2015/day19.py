from collections import defaultdict
import re

with open('inputs/2015/day19.txt','r') as file:
    replacements, genome = file.read().split('\n\n')
    replacements = replacements.split('\n')

genes = defaultdict(list)
revgenes = {}
for source,dest in [x.split(' => ') for x in replacements]:
    genes[source].append(dest)
    revgenes[dest] = source

# Part 1
new_genomes = []
for gene, dests in genes.items():
    for dest in dests:
        for m in re.finditer(gene, genome):
            new_genomes.append(genome[:m.start()] + dest + genome[m.end():])
print(len(set(new_genomes)))

# Part 2
unique_ancestors = set()
def find_ancestor(genome, revgenes):
    for gene, prevgene in revgenes.items():
        for m in re.finditer(gene, genome):
            ancestor = genome[:m.start()] + prevgene + genome[m.end():]
            #print("uniques: ", len(unique_ancestors))
            #if ancestor not in unique_ancestors:
            unique_ancestors.add((ancestor))
            yield ancestor

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    return total_path

# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def astar(start, goal, revgenes):
    import heapq
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = [(0,start)]

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from the start
    # to n currently known.
    cameFrom = {}

    # For node n, gScore[n] is the currently known cost of the cheapest path from start to n.
    gScore = defaultdict(lambda: 100000)
    gScore[start] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how cheap a path could be from start to finish if it goes through n.
    fScore = defaultdict(lambda: 100000)
    fScore[start] = gScore[start] #- len(start)/10

    while openSet:
        print(len(openSet), openSet)
        # This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        # current := the node in openSet having the lowest fScore[] value
        costcurrent, current = heapq.heappop(openSet)
        if current == goal:
            return reconstruct_path(cameFrom, current)

        for neighbor in find_ancestor(current,revgenes):
            #if any(item[1] == neighbor for item in openSet):
            #    continue

            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current

            tentative_gScore = gScore[current] + 1
            if tentative_gScore < gScore[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + len(neighbor)
                if neighbor not in openSet:
                    #openSet.add(neighbor)
                    print(f"adding {(fScore[neighbor], gScore[neighbor], neighbor)}" )
                    heapq.heappush(openSet, (fScore[neighbor], neighbor))

    # Open set is empty but goal was never reached
    return 0

print(len(astar(genome, 'e', revgenes)))

#print(astar('NRnFArTiMg', 'e', revgenes))
