import re

import numpy as np


def get_input(x):
    a = re.compile(r'A: X\+(\d*), Y\+(\d*)')
    b = re.compile(r'B: X\+(\d*), Y\+(\d*)')
    prize = re.compile(r'X=(\d*), Y=(\d*)')

    return list(zip(re.findall(a, x), re.findall(b, x), re.findall(prize, x)))


with open('inputs/2024/day13.txt', 'r') as file:
    raw = file.read()
problems = get_input(raw)


def solve(problems, offset):
    sum = 0
    for prob in problems:
        a = np.array([[int(prob[0][0]), int(prob[1][0])], [int(prob[0][1]), int(prob[1][1])]])
        b = np.array([offset + int(prob[2][0]), offset + int(prob[2][1])])
        sol = np.linalg.solve(a, b)

        if sol[0].is_integer() and sol[1].is_integer():

            sum += sol[0] * 3
            sum += sol[1]
        elif abs(sol[0] - round(sol[0])) < 0.0001 and abs(sol[1] - round(sol[1])) < 0.0001:

            sum += int(round(sol[0])) * 3
            sum += int(round(sol[1]))
    return sum


print(solve(problems, 0))
print(solve(problems, 10000000000000))
