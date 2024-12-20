import numpy as np

with open('inputs/2024/day4.txt', 'r') as file:
    x = [list(x) for x in file.read().split('\n')]

matrix = np.array(x)

cnts = 0
for i in range(4):

    matrix = np.rot90(matrix, i)
    for row in matrix:
        cnts += ''.join(row).count('XMAS')
    for idx in range(-len(matrix), len(matrix)):
        cnts += ''.join(matrix.diagonal(idx)).count('XMAS')
print(cnts)

cnts2 = 0
matrix = np.rot90(matrix, 1)
for yy, row in enumerate(x):
    for xx, char in enumerate(row):
        try:
            if char == 'A':
                if yy - 1 < 0 or xx - 1 < 0:
                    raise IndexError
                a = x[yy - 1][xx - 1]
                b = x[yy - 1][xx + 1]
                diagb = x[yy + 1][xx - 1]
                diaga = x[yy + 1][xx + 1]
                if a == diaga:
                    continue
                if b == diagb:
                    continue
                if [a, b, diaga, diagb].count('M') == 2 and [a, b, diaga, diagb].count('S') == 2:
                    cnts2 += 1
        except IndexError:
            continue
print(cnts2)
