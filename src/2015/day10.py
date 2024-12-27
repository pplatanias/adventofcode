from itertools import groupby

a = "1321131112"


def looks(inputstr, reps):
    for _ in range(reps):
        inputstr = ''.join([str(len(list(g))) + str(k) for k, g in groupby(inputstr)])
    return len(inputstr)


print(looks(a, 40))
print(looks(a, 50))
