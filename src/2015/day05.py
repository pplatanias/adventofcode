from itertools import pairwise

with open('inputs/2015/day5.txt', 'r') as file:
    rows = file.read().split('\n')

cnt = 0

# Part 1
for row in rows:
    doubles = False
    failing = False
    vowels = 0
    for ch in pairwise(row + '$'):
        if ch in [('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')]:
            failing = True
            break
        if ch[0] == ch[1]:
            doubles = True
        if ch[0] in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
    if doubles and vowels >= 3 and not failing:
        cnt += 1
print(cnt)

# Part 2
cnt = 0
for row in rows:
    triplet = False
    repeat = False
    for ch in zip(row, row[1:], row[2:]):
        if ch[0] == ch[2]:
            triplet = True
            break
    for id1 in range(len(row) - 1):
        if row[id1] + row[id1 + 1] in row[id1 + 2:]:
            repeat = True
            break
    if triplet and repeat:
        cnt += 1
print(cnt)
