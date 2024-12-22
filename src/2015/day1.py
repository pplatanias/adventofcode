with open('inputs/2015/day1.txt') as file:
    raw = file.read()

up = raw.count('(')
down = raw.count(')')
print(up - down)

floor = 0
for idx, ch in enumerate(raw):
    if ch == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        break

print(idx + 1)
