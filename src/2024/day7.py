from functools import partial, reduce
from itertools import product
from multiprocessing import Pool, cpu_count
from operator import mul


def get_input():
    with open('inputs/2024/day7.txt', 'r') as file:
        raw = file.read()
    x = raw.replace(':', '')
    x = [y.split() for y in x.split('\n')]
    x = [[int(y) for y in z] for z in x]
    return x


def ssum(a, b):
    return a + b


def cc(a, b):
    return int(''.join([str(a), str(b)]))


class Runner:

    def __init__(self):
        self.current = 0

    def run_next_action(self, a, b, actions):
        next = actions[self.current]
        self.current += 1
        return next(a, b)


def solve_1(inp):
    summer = 0
    for row in inp:
        actionslist = list(product([ssum, mul], repeat=len(row) - 2))
        for actions in actionslist:
            runner = Runner()
            run = partial(runner.run_next_action, actions=actions)
            result = reduce(run, row[1:])
            if result == row[0]:
                summer += result
                break
    return summer


def rowsolver(row):
    actionslist = list(product([ssum, mul, cc], repeat=len(row) - 2))
    for actions in actionslist:
        runner = Runner()
        run = partial(runner.run_next_action, actions=actions)
        result = reduce(run, row[1:])
        if result == row[0]:
            return result
    return 0


if __name__ == '__main__':

    print(solve_1(get_input()))

    res = 0
    with Pool(cpu_count()) as p:
        res = p.map(rowsolver, get_input())
    print(sum(res))
