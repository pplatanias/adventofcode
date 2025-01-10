from itertools import batched

with open('inputs/2016/day3.txt', 'r') as file:
    matrix = [[int(y) for y in x.split()] for x in file.read().split('\n')]

# Part 1
impossible = 0
for row in matrix:
    if max(row) < (sum(row) - max(row)):
        impossible += 1
print(impossible)

# Part 2
rows = len(matrix)
cols = len(matrix[0])
transposed = [[0 for _ in range(rows)] for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        transposed[j][i] = matrix[i][j]

impossible = 0
for row in transposed:
    for triangle in batched(row, 3):
        if max(triangle) < (sum(triangle) - max(triangle)):
            impossible += 1
print(impossible)
