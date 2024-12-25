import numpy as np

with open('inputs/2024/day25.txt','r') as file:
    text = file.read()
    text = text.replace('.','0').replace('#','1')
    things = text.split('\n\n')

locks = []
keys = []
for thing in things:
    lockorkey = np.array([list(map(int,list(x))) for x in thing.split('\n')])
    if lockorkey[0][0] == 0:
        keys.append(lockorkey)
    elif lockorkey[0][0] == 1:
        locks.append(lockorkey)

unique_matches = 0
for key in keys:
    for lock in locks:
        if all(sum(key+lock) <= 7):
            unique_matches +=1
print(unique_matches)

