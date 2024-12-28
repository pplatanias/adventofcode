from functools import reduce
from operator import mul

ingredients = [(4, -2, 0, 0, 5), (0, 5, -1, 0, 8), (-1, 0, 5, 0, 6), (0, 0, -2, 2, 1)]


def calc(dosages, ingredients):
    counter = [0] * len(ingredients[0])
    for ingredient_id, dosage in enumerate(dosages):
        for component_id, component in enumerate(ingredients[ingredient_id]):
            counter[component_id] += dosage * component
    return reduce(mul, [0 if x < 0 else x for x in counter[0:4]]), counter


# Use 'Maximize[{(4a-c)(-2a+5b)(-b+5c-2d)(2d), a+b+c+d=100}]' on wolfram alpha
print(calc([24, 29, 31, 16], [x[:-1] for x in ingredients])[0])

# The final constraint 5a+8b+6c+d=500 sets constraints for a,b,c at 100, 62, 83 respectively,
# significantly reducing the search space. So we iterate.
cur_max = 0
for a in range(1, 101):
    for b in range(1, min(100 - a, 63)):
        for c in range(1, min(100 - a - b, 84)):
            d = 100 - a - b - c
            if a + b + c + d == 100:
                result = calc([a, b, c, d], ingredients)
                if result[1][4] == 500:
                    if result[0] > cur_max:
                        cur_max = result[0]
print(cur_max)
