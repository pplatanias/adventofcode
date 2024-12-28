import re
from collections import defaultdict

with open('inputs/2015/day16.txt', 'r') as file:
    rows = file.read().split('\n')

sues = defaultdict(dict)
rexps = [
    r'children: (\d*)(?:,|$)',
    r'cats: (\d*)(?:,|$)',
    r'samoyeds: (\d*)(?:,|$)',
    r'pomeranians: (\d*)(?:,|$)',
    r'akitas: (\d*)(?:,|$)',
    r'vizslas: (\d*)(?:,|$)',
    r'goldfish: (\d*)(?:,|$)',
    r'trees: (\d*)(?:,|$)',
    r'cars: (\d*)(?:,|$)',
    r'perfumes: (\d*)(?:,|$)',
]
for row_id, row in enumerate(rows):
    for rexp in rexps:
        key = rexp.split(':')[0]
        result = re.findall(rexp, row)
        if result:
            sues[row_id + 1][key] = int(result[0])

# Part 1
requirement = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}
for sue, sue_items in sues.items():
    # The get default value is so that sues without known quantity for an item return True in the all.
    if all(sue_items.get(req_name, req_num) == req_num for req_name, req_num in requirement.items()):
        print(sue)

# Part 2
requirement_2 = {
    'children': lambda x: x == 3 if x is not None else True,
    'cats': lambda x: x > 7 if x is not None else True,
    'samoyeds': lambda x: x == 2 if x is not None else True,
    'pomeranians': lambda x: x < 3 if x is not None else True,
    'akitas': lambda x: x == 0 if x is not None else True,
    'vizslas': lambda x: x == 0 if x is not None else True,
    'goldfish': lambda x: x < 5 if x is not None else True,
    'trees': lambda x: x > 3 if x is not None else True,
    'cars': lambda x: x == 2 if x is not None else True,
    'perfumes': lambda x: x == 2 if x is not None else True,
}
for sue, sue_items in sues.items():
    if all(req_func(sue_items.get(req_name, None)) for req_name, req_func in requirement_2.items()):
        print(sue)
