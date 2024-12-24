import re


def do_operation(l_op, cmd, r_op):
    if cmd == 'AND':
        return l_op & r_op
    elif cmd == 'OR':
        return l_op | r_op
    elif cmd == 'XOR':
        return l_op ^ r_op


with open('inputs/2024/day24.txt', 'r') as file:
    starting, cmdrows = file.read().split('\n\n')

register = {x.split(': ')[0]: int(x.split(': ')[1]) for x in starting.split('\n')}

cmds = []
for row in cmdrows.split('\n'):
    left, out = row.split(' -> ')
    l_op, cmd, r_op = re.split(r' (XOR|OR|AND) ', left)
    cmds.append((l_op, cmd, r_op, out))
    register[out] = None

target_out = sorted([key for key in register.keys() if key.startswith('z')], reverse=True)

# Part 1
curr_cmds = [cmd for cmd in cmds]
while True:
    next_cmds = []
    for l_op, cmd, r_op, out in curr_cmds:
        l_val = register.get(l_op)
        r_val = register.get(r_op)

        if l_val is not None and r_val is not None:
            register[out] = do_operation(l_val, cmd, r_val)
        else:
            next_cmds.append((l_op, cmd, r_op, out))
        curr_cmds = next_cmds
    if all([register.get(z_target) is not None for z_target in target_out]):
        break
print(int(''.join(map(str, [register[zkey] for zkey in target_out])), 2))

# Part 2
with open('inputs/2024/day24modified.txt', 'r') as file:
    starting, cmdrows = file.read().split('\n\n')

cmds = []
for row in cmdrows.split('\n'):
    left, out = row.split(' -> ')
    l_op, cmd, r_op = re.split(r' (XOR|OR|AND) ', left)
    cmds.append((l_op, cmd, r_op, out))

c_wires = [None] * 45
s_wires = [None] * 45
fa_xor_1 = [None] * 44
fa_and_1 = [None] * 44
fa_and_2 = [None] * 44
lists = [c_wires, s_wires, fa_and_1, fa_and_2, fa_and_2]


def find_ith_full_adder(cmds, n):
    nn = format(n, '02')
    xnn = 'x' + nn
    ynn = 'y' + nn

    s_wire_found = False
    c_wire_found = False
    fa_xor_1_found = False
    fa_and_1_found = False
    fa_and_2_found = False

    quintuple_cmds = [x for x in cmds] * 5
    for l_op, cmd, r_op, out in quintuple_cmds:
        if l_op in [xnn, ynn] and r_op in [xnn, ynn] and cmd == 'XOR':
            if n != 0:
                fa_xor_1[n] = out
                fa_xor_1_found = True
            else:
                s_wires[0] = out
                s_wire_found = True

        if l_op in [xnn, ynn] and r_op in [xnn, ynn] and cmd == 'AND':
            if n != 0:
                fa_and_1[n] = out
                fa_and_1_found = True
            else:
                c_wires[0] = out
                c_wire_found = True

        reqs = [fa_xor_1[n], c_wires[n - 1]]
        if all(reqs) and l_op in reqs and r_op in reqs and cmd == 'XOR':
            s_wires[n] = out
            s_wire_found = True

        if all(reqs) and l_op in reqs and r_op in reqs and cmd == 'AND':
            fa_and_2[n] = out
            fa_and_2_found = True

        reqs = [fa_and_2[n], fa_and_1[n]]
        if all(reqs) and l_op in reqs and r_op in reqs and cmd == 'OR':
            c_wires[n] = out
            c_wire_found = True

    if n > 0 and not all([s_wire_found, c_wire_found, fa_xor_1_found, fa_and_1_found, fa_and_2_found]):
        return False
    else:
        return True


for i in range(44):
    found = find_ith_full_adder(cmds, i)
    x = max(0, i - 5)
    if not found:
        print(f'NOT FOUND at {i}')

        # Inspect the state of the last full adder and correct mistakes on day24modified.txt
        print(f'c_wires: {c_wires[x:i+2]}')
        print(f's_wires: {s_wires[x:i+2]}')
        print(f'fa_xor_1: {fa_xor_1[x:i+2]}')
        print(f'fa_and_1: {fa_and_1[x:i+2]}')
        print(f'fa_and_2: {fa_and_2[x:i+2]}')
        break

# z07 <-> nqk
# fgt <-> pcp
# fpq <-> z24
# z32 <-> srn

swaps = ['z07', 'nqk', 'fgt', 'pcp', 'fpq', 'z24', 'z32', 'srn']
print(','.join(sorted(swaps)))
