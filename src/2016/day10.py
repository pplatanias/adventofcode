import re
from collections import defaultdict

with open('inputs/2016/day10.txt', 'r') as file:
    cmds = file.read().split('\n')

funcs = defaultdict(list)

while cmds:
    for cmd in cmds:
        if cmd.startswith('value '):
            val, bot = cmd[6:].split(' goes to ')
            funcs[bot].append(int(val))
            cmds.remove(cmd)

        if cmd.startswith('bot '):
            source, rest = cmd.split(' gives low to ')
            dest_1, dest_2 = rest.split(' and high to ')
            if len(funcs[source])==2:
                outtype1, outid1 = dest_1.split()
                outtype2, outid2 = dest_2.split()
                in_1 = funcs[source][0]
                in_2 = funcs[source][1]
                # Part 1
                if 61 in [in_1,in_2] and 17 in [in_1,in_2]:
                    print(cmd)
                funcs[dest_1].append(min((int(in_1),int(in_2))))
                funcs[dest_2].append(max((int(in_1),int(in_2))))
                cmds.remove(cmd)

print(funcs['output 0'][0] * funcs['output 1'][0] * funcs['output 2'][0])