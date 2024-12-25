import re

with open('inputs/2015/day2.txt') as file:
    raw = file.read()

boxes = re.findall(r'(\d*)x(\d*)x(\d*)', raw)
boxes = [(int(box[0]), int(box[1]), int(box[2])) for box in boxes]

sum = 0
for x, y, z in boxes:
    sum += (2 * (x * y + y * z + x * z) + min([x * y, y * z, x * z]))
print(sum)

sum = 0
for x, y, z in boxes:
    min_side = 2 * x + 2 * y + 2 * z - 2 * max([x, y, z])
    ribbon = x * y * z
    sum += min_side + ribbon
print(sum)
