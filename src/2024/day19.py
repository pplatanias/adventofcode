from functools import lru_cache


def get_input():
    with open('inputs/2024/day19.txt', 'r') as file:
        x = file.read()
    x = x.split('\n')
    towels = x[0].split(', ')
    combos = x[2:]
    return tuple(towels), combos


@lru_cache(maxsize=None)
def check_combo(combo, towels):
    if not combo:
        return 1

    for t in towels:
        if combo.startswith(t):
            if check_combo(combo[len(t):], towels):
                return 1

    return 0


@lru_cache(maxsize=None)
def check_all_combo(combo, towels):
    if not combo:
        return 1

    found = 0
    for t in towels:
        if combo.startswith(t):
            found += check_all_combo(combo[len(t):], towels)

    if found:
        return found
    else:
        return 0


def part1():
    towels, combos = get_input()
    possibles = 0
    for combo in combos:
        possibles += check_combo(combo, towels)
    return possibles


def part2():
    towels, combos = get_input()
    possibles = 0
    for combo in combos:
        possibles += check_all_combo(combo, towels)
    return possibles


print(part1())
print(part2())
