with open('inputs/2016/day1.txt','r') as file:
    steps = file.read().split(', ')

# Part 1
def solve_1():
    loc = [0,0]
    direction = [1,0]
    for step in steps:
        if step[0] == 'L':
            direction[0], direction[1] = direction[1], -1*direction[0]
        if step[0] == 'R':
            direction[0], direction[1] = -1*direction[1], direction[0]
        dist=int(step[1:])
        loc[0] += direction[0]*dist
        loc[1] += direction[1]*dist
    return abs(loc[0]-0) + abs(loc[1]-0)


# Part 2
def solve_2():
    direction = [1,0]
    visited = [[0,0]]
    for step in steps:
        if step[0] == 'L':
            direction[0], direction[1] = direction[1], -1*direction[0]
        if step[0] == 'R':
            direction[0], direction[1] = -1*direction[1], direction[0]
        dist=int(step[1:])
        for _ in range(dist):
            next_node = [visited[-1][0] + direction[0], visited[-1][1] + direction[1]]
            if next_node in visited:
                return next_node, abs(next_node[0]-0) + abs(next_node[1]-0)
            else:
                visited.append(next_node)

print(solve_1())
print(solve_2())
