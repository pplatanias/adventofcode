import re

two_operand_cmds = ['AND', 'OR', 'LSHIFT', 'RSHIFT']


def do_operation(in_1, cmd, in_2, out_label):
    if in_1 is not None:
        if not isinstance(in_1, int):
            in_1 = register.get(in_1, None)
            if in_1 is None:
                return

    if in_2 is not None:
        if not isinstance(in_2, int):
            in_2 = register.get(in_2, None)
            if in_2 is None:
                return

    if cmd == 'AND':
        out = in_1 & in_2
    if cmd == 'LSHIFT':
        out = in_1 << in_2
    if cmd == 'RSHIFT':
        out = in_1 >> in_2
    if cmd == 'OR':
        out = in_1 | in_2
    if cmd == 'NOT':
        out = ~in_2 & int('1' * 16, 2)
    if cmd is None:
        out = in_1

    register[out_label] = out


def cmdparser(cmdrow):
    l_operand, cmd, r_operand = None, None, None

    left, _, out = cmdrow.partition(' -> ')
    if 'NOT' in left:
        _, cmd, r_operand = left.partition('NOT ')
        cmd = cmd.strip()
    elif any(two_op_cmd in left for two_op_cmd in two_operand_cmds):
        l_operand, cmd, r_operand = re.split(r' (AND|LSHIFT|RSHIFT|OR) ', left)
    else:
        l_operand = left

    return l_operand, cmd, r_operand, out


# Part 1
with open('inputs/2015/day7.txt', 'r') as file:
    rows = file.read().split('\n')

cmds = []
for cmdrow in rows:
    cmds.append(cmdparser(cmdrow))

register = {}
register['a'] = 'unsolved'
while not register.get('a').isnumeric():
    for l_operand, cmd, r_operand, out in cmds:
        if l_operand and l_operand.isnumeric():
            l_operand = int(l_operand)
        if r_operand and r_operand.isnumeric():
            r_operand = int(r_operand)
        do_operation(l_operand, cmd, r_operand, out)

    if isinstance(register['a'], int):
        break

part_1_a = str(register['a'])
print(part_1_a)

# Part 2
with open('inputs/2015/day7.txt', 'r') as file:
    rows = file.read().replace('14146', part_1_a).split('\n')

cmds = []
for cmdrow in rows:
    cmds.append(cmdparser(cmdrow))

register = {}
register['a'] = 'unsolved'
while not register.get('a').isnumeric():
    for l_operand, cmd, r_operand, out in cmds:
        if l_operand and l_operand.isnumeric():
            l_operand = int(l_operand)
        if r_operand and r_operand.isnumeric():
            r_operand = int(r_operand)
        do_operation(l_operand, cmd, r_operand, out)

    if isinstance(register['a'], int):
        break
print(register['a'])
