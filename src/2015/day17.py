from itertools import combinations

a = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]

# Part 1
combos = 0
for i in range(20):
    all_ith_combos = combinations(a, i)
    for combo in all_ith_combos:
        if sum(combo) == 150:
            combos += 1
print(combos)

# Part 2
combos = 0
for i in range(20):
    all_ith_combos = combinations(a, i)
    for combo in all_ith_combos:
        if sum(combo) == 150:
            combos += 1
    if combos:
        break
print(combos, i)
