with open('inputs/2016/day06.txt', 'r') as file:
    matrix = [list(x) for x in file.read().split('\n')]

rows = len(matrix)
cols = len(matrix[0])
transposed = [[0 for _ in range(rows)] for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        transposed[j][i] = matrix[i][j]

# Part 1
msg = []
for row in transposed:
    group = sorted(row, key=lambda x: row.count(x), reverse=True)
    msg.append(group[0])
print(''.join(msg))

# Part 2
msg = []
for row in transposed:
    group = sorted(row, key=lambda x: row.count(x))
    msg.append(group[0])
print(''.join(msg))
