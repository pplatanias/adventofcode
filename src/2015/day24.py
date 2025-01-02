from itertools import combinations
from math import prod

with open('inputs/2015/day24.txt') as file:
    packages = [int(x) for x in file.read().split('\n')]
packages = sorted(packages,reverse=True)

def solve_a():
    solutions = []
    third = sum(packages) / 3
    for i in range(1,len(packages)):
        fronts = list(combinations(packages, i))
        for front in fronts:
            if sum(front) == third:
                rest = list(set(packages) - set(front))
                #import pdb; pdb.set_trace()
                for j in range(len(rest)):
                    lefts = combinations(rest,j)
                    for left in lefts:
                        if sum(left) == third:
                            right = list(set(rest) - set(left))
                            if sum(left) == sum(right) == sum(front):
                                solutions.append((len(front),prod(front)))
                                return solutions

class CursedBreak(Exception):
    pass

def solve_b():
    solutions = []
    fourth = sum(packages) / 4
    for i in range(1,len(packages)):
        fronts = list(combinations(packages, i))
        for front in fronts:
            try:
                if sum(front) == fourth:
                    leftrightbot = list(set(packages) - set(front))
                    for j in range(len(leftrightbot)):
                        lefts = combinations(leftrightbot,j)
                        for left in lefts:
                            if sum(left) == fourth:
                                rightbot = list(set(leftrightbot) - set(left))
                                for z in range(len(rightbot)):
                                    rights = combinations(rightbot,z)
                                    for right in rights:
                                        if sum(right) == fourth:
                                            bot = list(set(rightbot) - set(right))
                                            if sum(left) == sum(right) == sum(front) == sum(bot):
                                                if solutions and solutions[-1][0] < len(front):
                                                    return solutions
                                                solutions.append((len(front),prod(front)))
                                                raise CursedBreak  # skip to next front

            except CursedBreak:
                # This is some cursed flow control.
                continue

    return solutions

sols = solve_a()
print(sorted(sols)[0])

sols = solve_b()
print(sorted(sols)[0])
