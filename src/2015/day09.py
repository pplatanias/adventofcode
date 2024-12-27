import re
import time
from functools import cache
from itertools import combinations


@cache
def heldkarp(start, cities, min_=True):
    "Recursive held-karp from given start, without returning to start"

    if len(cities) == 1:
        return edges[start, cities[0]], cities

    candis = []
    for route in combinations(cities, len(cities) - 1):
        last = (set(cities) - set(route)).pop()

        res = heldkarp(start, route, min_=min_)
        totres = res[0] + edges[(res[1][-1], last)]
        candis.append((totres, res[1] + (last,)))
    if min_:
        return min(candis)
    else:
        return max(candis)


with open('inputs/2015/day9.txt') as file:
    rexp = re.compile(r'^(.*) to (.*) = (.*)$', re.MULTILINE)
    rows = re.findall(rexp, file.read())

edges = {}
cities = set()
for s, e, dist in rows:
    edges[(s, e)] = int(dist)
    edges[(e, s)] = int(dist)
    cities.update([s, e])

# Part 1 Held-Karp
now = time.time()
res = []
for curr_city in cities:
    cpcities = tuple(city for city in cities if city != curr_city)
    result = heldkarp(curr_city, cpcities, min_=True)
    res.append((result[0], (curr_city,) + result[1]))
print(min(res))
print(time.time() - now)

# Part 2 Held-Karp
now = time.time()
res = []
for curr_city in cities:
    cpcities = tuple(city for city in cities if city != curr_city)
    result = heldkarp(curr_city, cpcities, min_=False)
    res.append((result[0], (curr_city,) + result[1]))
print(max(res))
print(time.time() - now)
