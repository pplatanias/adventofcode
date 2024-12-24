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
while curr_cmds:
    # Loop through commands executing ones that are able to run and removing them
    # from future loops.
    next_cmds = []
    for l_op, cmd, r_op, out in curr_cmds:
        l_val = register.get(l_op)
        r_val = register.get(r_op)

        if l_val is not None and r_val is not None:
            register[out] = do_operation(l_val, cmd, r_val)
        else:
            next_cmds.append((l_op, cmd, r_op, out))
        curr_cmds = next_cmds
print(int(''.join(map(str, [register[zkey] for zkey in target_out])), 2))

# Part 2
with open('inputs/2024/day24.txt', 'r') as file:
    starting, cmdrows = file.read().split('\n\n')

cmds = []
for row in cmdrows.split('\n'):
    left, out = row.split(' -> ')
    l_op, cmd, r_op = re.split(r' (XOR|OR|AND) ', left)
    cmds.append((l_op, cmd, r_op, out))

# Lists of full adder components, each adder tracked by index n
c_wires = [None] * 45
s_wires = [None] * 45
fa_xor_1 = [None] * 44
fa_and_1 = [None] * 44
fa_and_2 = [None] * 44
lists = [c_wires, s_wires, fa_and_1, fa_and_2, fa_and_2]


def find_nth_full_adder(cmds, n):
    nn = format(n, '02')
    xnn = 'x' + nn
    ynn = 'y' + nn

    s_wire_found = False
    c_wire_found = False
    fa_xor_1_found = False
    fa_and_1_found = False
    fa_and_2_found = False

    # commands are not sorted so for 5 components we need to loop at worst 5 times.
    quintuple_cmds = [x for x in cmds] * 5
    for l_op, cmd, r_op, out in quintuple_cmds:
        if l_op in [xnn, ynn] and r_op in [xnn, ynn] and cmd == 'XOR':
            if n != 0:
                fa_xor_1[n] = out
                fa_xor_1_found = True
            else:
                # Initial half-adder
                s_wires[0] = out
                s_wire_found = True

        if l_op in [xnn, ynn] and r_op in [xnn, ynn] and cmd == 'AND':
            if n != 0:
                fa_and_1[n] = out
                fa_and_1_found = True
            else:
                # Initial half-adder
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


for n in range(44):
    found = find_nth_full_adder(cmds, n)
    x = max(0, n - 5)
    if not found:
        print(f'Full adder {n} not found')

        # Inspect the state of the last full adder and correct mistakes on day24modified.txt
        # The patters should stand out pretty easily.
        print(f'c_wires : {c_wires[x:n+2]}')
        print(f's_wires : {s_wires[x:n+2]}')
        print(f'fa_xor_1: {fa_xor_1[x:n+2]}')
        print(f'fa_and_1: {fa_and_1[x:n+2]}')
        print(f'fa_and_2: {fa_and_2[x:n+2]}')
        break

# z07 <-> nqk
# fgt <-> pcp
# fpq <-> z24
# z32 <-> srn

swaps = ['z07', 'nqk', 'fgt', 'pcp', 'fpq', 'z24', 'z32', 'srn']
print(','.join(sorted(swaps)))
