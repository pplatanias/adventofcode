
from itertools import combinations
from random import shuffle
from copy import deepcopy

def find_moves(floors):
    curr_floor = [i for i,floor in enumerate(floors) if 'E' in floor][0]
    moves = []
    for i in range(1,3):
        for j in [curr_floor+1, curr_floor-1]:
            if j >= 0 and j <=3:
                for move in list(combinations(floors[curr_floor][1:],i)):
                    moves.append([curr_floor, j,'E'] + list(move))
    moves = [move for move in moves if is_valid_move(move,floors)]
    return moves

def is_valid_move(move,floors):
    leaving_floor = [x for x in floors[move[0]] if x not in move[2:]]
    entering_floor = floors[move[1]] + move[2:]
    if all(is_valid_floor(floor) for floor in (leaving_floor, entering_floor)):
        return True

def is_valid_floor(floor):
    return all(is_valid_microchip(thing, floor) for thing in floor if thing[0]=='M')

def is_valid_microchip(microchip,floor):
    return ('G'+microchip[1] in floor or not any(x for x in floor if x[0]=='G'))

def commit_move(move,floors):
    if any(floor.count('E')>1 for floor in floors):
        import pdb; pdb.set_trace()
    floors[move[0]] = [thing for thing in floors[move[0]] if thing not in move[2:]]
    floors[move[1]] = floors[move[1]] + move[2:]
    floors[move[1]].sort()


allmoves = set()
def solve(floors, maxdepth=0, prevmove = None):
    if len(floors[3]) == 11:
        return 1, True

    if maxdepth == 0:
        return 10000000, False

    moves = find_moves(floors)
    steps = []

    if not moves:
        return 10000000, False
    print(len(floors[3]))
    for move in moves:
        if prevmove and prevmove[2:] == move[2:] and prevmove[0] == move[1] and prevmove[1] == move[0]:
            continue
        nextfloors = deepcopy(floors)
        commit_move(move, nextfloors)
        steps.append(solve(deepcopy(nextfloors), maxdepth-1, move))

    if not steps:
        return 1000000, False
    return min(steps)

floors = [
    ['E','G0','M0'],
    ['G1','G2','G3','G4'],
    ['M1','M2','M3','M4'],
    [],
]

a = ['1'*50]*50
for row in a:
    print(row)
b = [11111111111]
print('*')
#print(solve(floors,maxdepth=10))