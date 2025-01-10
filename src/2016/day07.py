import re
from itertools import chain, product

with open('inputs/2016/day07.txt', 'r') as file:
    rows = file.read().split('\n')


def is_tls(s):
    for i in range(len(s) - 3):
        if s[i + 2] == s[i + 1] and s[i + 3] == s[i] and s[i] != s[i + 1]:
            return True


def get_ababs(s):
    abas = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and s[i] != s[i + 1]:
            abas.append(s[i:i + 3])
    return abas


def is_ssl(abas, babs):
    for i in product(abas, babs):
        if i[0][0] == i[1][1] and i[0][1] == i[1][0]:
            return True, i


# Part 1
total = 0
for row in rows:
    excludes = re.findall(r'(\[.*?\])', row)
    includes = re.findall(r'^(.*?)\[', row)
    includes.extend(re.findall(r'\](.*?)\[', row))
    includes.extend(re.findall(r'\]([^\]\[]*?)$', row))
    print(includes, excludes)
    if any(is_tls(x) for x in includes) and not any(is_tls(x) for x in excludes):
        total += 1
print(total)

# Part 2
total = 0
for row in rows:
    excludes = re.findall(r'(\[.*?\])', row)
    includes = re.findall(r'^(.*?)\[', row)
    includes.extend(re.findall(r'\](.*?)\[', row))
    includes.extend(re.findall(r'\]([^\]\[]*?)$', row))
    all_abas = list(chain(*[get_ababs(x) for x in includes]))
    all_babs = list(chain(*[get_ababs(x) for x in excludes]))
    if is_ssl(all_abas, all_babs):
        total += 1
print(total)
