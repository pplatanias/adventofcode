import re
from itertools import groupby

with open('inputs/2016/day4.txt', 'r') as file:
    rows = re.findall(r'(.*-)(\d*)\[(.*)\]', file.read())

# Part 1
total = 0
new_rows = []
for room in rows:
    group = sorted(sorted(room[0].replace('-', '')), key=lambda x: room[0].count(x), reverse=True)
    crc = ''.join(list({x: None for x in group})[0:5])
    if crc == room[2]:
        total += int(room[1])
        new_rows.append(room)
print(total)

# Part 2
decrypted = []
for room in new_rows:
    new_name = ''
    offset = int(room[1])
    for ch in room[0]:
        if ch == '-':
            new_name += ch
        else:
            start = offset - (26 - (ord(ch) - ord('a')))
            modded = start % 26
            new_name += chr(ord('a') + modded)
    decrypted.append((new_name, room[1]))

[print(x) for x in decrypted if 'north' in x[0]]
