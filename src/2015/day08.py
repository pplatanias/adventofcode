from ast import literal_eval

with open('inputs/2015/day8.txt', 'r') as file:
    lines = file.read().split()

sum_ = 0
for line in lines:
    sum_ += (len(line) - len(literal_eval(line)))
print(sum_)

sum_ = 0
for line in lines:
    # Repr wont work here, because python doesn't need to escape the " characters.
    sum_ += line.count('"') + line.count('\\') + 2
print(sum_)
