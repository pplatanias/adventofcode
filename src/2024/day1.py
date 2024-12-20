with open('inputs/2024/day1.txt', 'r') as file:
    raw = [x.split() for x in file.read().split('\n')]

left = []
right = []
for z, i in raw:
    left.append(z)
    right.append(i)

left.sort()
right.sort()
sum = 0
for x, y in zip(left, right):
    sum += abs(int(x) - int(y))
print(sum)

ssum = 0
for num in left:
    ssum += int(num) * int(right.count(num))
print(ssum)
