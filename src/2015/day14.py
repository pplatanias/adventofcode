import re

with open('inputs/2015/day14.txt', 'r') as file:
    rows = re.findall(r' can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.', file.read())
    rows = [(int(x[0]), int(x[1]), int(x[2])) for x in rows]

# Part 1
delta = []
for idrow, row in enumerate(rows):
    speed, duration, sleep = row
    speedcycles, remainder = divmod(2503, duration + sleep)
    delta.append((speedcycles * speed * duration + min(remainder, duration) * speed, idrow))
print(max(delta))

# Part 2
# Cant figure out a trick to avoid iterating over seconds
scores = [0] * len(rows)
for i in range(2503):
    delta = []
    for idrow, row in enumerate(rows):
        speed, duration, sleep = row
        speedcycles, remainder = divmod(i + 1, duration + sleep)
        delta.append((speedcycles * speed * duration + min(remainder, duration) * speed, idrow))
    winners = [x for x in delta if x[0] == max(delta)[0]]

    for _, winner_id in winners:
        scores[winner_id] += 1
print(max(scores))
