import re

with open('inputs/2024/day3.txt', 'r') as file:
    raw = file.read()

rexp = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
print(sum([int(pair[0]) * int(pair[1]) for pair in re.findall(rexp, raw)]))

rexp1 = re.compile(r"don't\(\).*?do\(\)")
while True:
    substr = re.search(rexp1, raw)
    if substr:
        raw = raw.replace(substr.group(), 'xxxxxxx', 1)
    else:
        rexp2 = re.compile(r"don't\(\).*$")
        substr = re.search(rexp2, raw)
        if substr:
            raw = raw.replace(substr.group(), 'xxxxxxx', 1)
        break

rexp = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
print(sum([int(pair[0]) * int(pair[1]) for pair in re.findall(rexp, raw)]))
