import re


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


def rect(matrix, y, x):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < y and j < x:
                matrix[i][j] = '1'


def rot(matrix, y, steps):
    row = ''.join(matrix[y])
    realsteps = steps % len(matrix[y])
    new_row = row[-realsteps:] + row[:-realsteps]
    matrix[y] = list(new_row)


with open('inputs/2016/day08.txt', 'r') as file:
    cmds = file.read().split('\n')

matrix = [['0' for _ in range(50)] for _ in range(6)]

for cmd in cmds:
    if 'rect' in cmd:
        x, y = re.findall('(\d*)x(\d*)', cmd)[0]
        rect(matrix, int(y), int(x))
    if 'rotate row' in cmd:
        y, steps = re.findall('y=(\d*) by (\d*)', cmd)[0]
        rot(matrix, int(y), int(steps))
    if 'rotate column' in cmd:
        y, steps = re.findall('x=(\d*) by (\d*)', cmd)[0]
        matrix = transpose(matrix)
        rot(matrix, int(y), int(steps))
        matrix = transpose(matrix)

# Part 1 & 2
total = 0
for r in matrix:
    print(''.join([x if x == '1' else '.' for x in r]))
    total += r.count('1')
print(total)
