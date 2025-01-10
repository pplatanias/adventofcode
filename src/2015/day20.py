from collections import defaultdict
from functools import cache
from itertools import count, groupby, product
from math import prod, sqrt


@cache
def find_divisors(num):
    top = int(sqrt(num))
    divisors = []
    for i in range(2, top + 1):
        if num % i == 0:
            divisors.append(i)
            cached_divisors = find_divisors(num // i)
            divisors.extend(cached_divisors)
            break
    else:
        return [num]
    return divisors


def expand_divisors(divisors):
    all_divs = set()
    to_product = []
    for divi in set(divisors):
        pproduct = []
        v = divisors.count(divi)
        for p in range(v + 1):
            pproduct.append(divi**p)
        to_product.append(pproduct)
    all_divs.update([prod(x) for x in product(*to_product)])
    return all_divs


def solve_a(threshold):
    for housenum in count(1, 1):
        divisors = find_divisors(housenum)
        divset = expand_divisors(divisors)
        if sum(divset) >= threshold:
            break
    return housenum


def solve_b(threshold):
    for housenum in count(1, 1):
        divisors = find_divisors(housenum)
        divset = expand_divisors(divisors)
        if sum([x for x in divset if housenum / x <= 50]) >= threshold:
            break
    return housenum


threshold = 34000000

print(solve_a(threshold / 10))
print(solve_b(threshold / 11))
