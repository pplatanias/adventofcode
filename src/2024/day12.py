from collections import defaultdict
from copy import deepcopy

with open('inputs/2024/day12.txt', 'r') as file:
    map = [y for y in file.read().split('\n')]

regions = []  # [[fencecount, letter, [coords1,coords2], [letter, fencecount, [coords1,coords2],]
fences = defaultdict
for idy, row in enumerate(map):
    for idx, ch in enumerate(row):

        current_regions = []
        for region in regions:
            if ch == region[1] and (idy, idx) in region[2]:
                # get region candidates
                current_regions.append(region)

        if not current_regions:
            current_regions = [[0, ch, [(idy, idx)]]]
            regions.append(current_regions[0])

        if len(current_regions) > 1:
            # merge region fencecounts and areas
            merge_region = [
                current_regions[0][0] + current_regions[1][0], current_regions[0][1],
                current_regions[0][2] + current_regions[1][2]
            ]
            regions.remove(current_regions[0])
            regions.remove(current_regions[1])
            regions.append(merge_region)
            current_region = merge_region
        else:
            current_region = current_regions[0]

        up = (idy - 1, idx)
        down = (idy + 1, idx)
        right = (idy, idx + 1)
        left = (idy, idx - 1)
        for dir in [left, right, up, down]:
            # out of bounds or other plant
            if (dir[0] < 0 or dir[0] >= len(map) or dir[1] < 0 or dir[1] >= len(map)) or map[dir[0]][dir[1]] != ch:
                current_region[0] += 1

            else:  # same region
                current_region[2].append((dir[0], dir[1]))

sum = 0
r = 0
for region in regions:
    sum += region[0] * len(set(region[2]))
print(sum)

gigaedges = 0

for region in regions:
    unvisited = deepcopy(sorted(list(set(region[2]))))
    newmap = []
    for i in range(len(map)):
        x = []
        for z in range(len(map[0])):
            x.append([])
        newmap.append(x)

    for idy, row in enumerate(map):
        if not unvisited:
            break
        for idx, ch in enumerate(row):
            if not unvisited:
                break

            if (idy, idx) in unvisited:
                unvisited.remove((idy, idx))

                up = (idy - 1, idx)
                down = (idy + 1, idx)
                right = (idy, idx + 1)
                left = (idy, idx - 1)

                # out of bounds or other plant
                if (up[0] < 0 or up[0] >= len(map) or up[1] < 0
                        or up[1] >= len(map)) or (up[0], up[1]) not in region[2]:
                    newmap[idy][idx].append('u')
                if (left[0] < 0 or left[0] >= len(map) or left[1] < 0
                        or left[1] >= len(map)) or (left[0], left[1]) not in region[2]:
                    newmap[idy][idx].append('l')
                if (right[0] < 0 or right[0] >= len(map) or right[1] < 0
                        or right[1] >= len(map)) or (right[0], right[1]) not in region[2]:
                    newmap[idy][idx].append('r')
                if (down[0] < 0 or down[0] >= len(map) or down[1] < 0
                        or down[1] >= len(map)) or (down[0], down[1]) not in region[2]:
                    newmap[idy][idx].append('d')

    edges = 0

    unvisited = deepcopy(sorted(list(set(region[2]))))

    for idy, row in enumerate(newmap):
        prev_u = False
        prev_d = False
        if not unvisited:
            break
        for idx, ch in enumerate(row):
            if not unvisited:
                break
            if (idy, idx) in unvisited:
                unvisited.remove((idy, idx))

                if 'u' in newmap[idy][idx]:
                    if prev_u is False:
                        edges += 1
                    prev_u = True
                else:
                    prev_u = False

                if 'd' in newmap[idy][idx]:
                    if prev_d is False:
                        edges += 1
                    prev_d = True
                else:
                    prev_d = False

            else:
                prev_u = False
                prev_d = False

    unvisited = deepcopy(sorted(list(set(region[2]))))

    for idx in range(len(newmap)):
        if not unvisited:
            break
        prev_l = False
        prev_r = False
        for idy in range(len(newmap)):
            if not unvisited:
                break
            if (idy, idx) in unvisited:
                unvisited.remove((idy, idx))

                if 'l' in newmap[idy][idx]:
                    if prev_l is False:
                        edges += 1

                    prev_l = True
                else:
                    prev_l = False

                if 'r' in newmap[idy][idx]:
                    if prev_r is False:
                        edges += 1

                    prev_r = True
                else:
                    prev_r = False

            else:
                prev_r = False
                prev_l = False

    gigaedges += edges * len(set(region[2]))

print(gigaedges)
