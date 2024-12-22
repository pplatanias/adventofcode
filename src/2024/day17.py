import math
import re


def parse_text(text):
    exp = re.compile(r'(\d*)')
    numbers = [x for x in re.findall(exp, text) if x]
    return numbers[0], numbers[1], numbers[2], numbers[3:]


class Compiler:

    def __init__(self, a, b, c, commands, debug=False):
        self.A = int(a)
        self.B = int(b)
        self.C = int(c)
        self.debug = debug
        self.commands = commands
        self.buffer = []

    def get_combo_value(self, operand):
        opmap = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': self.A,
            '5': self.B,
            '6': self.C,
            '7': self.cdv,
        }
        return opmap[operand]

    def get_cmd(self, cmdcode):
        cmdmap = {
            '0': self.adv,
            '1': self.bxl,
            '2': self.bst,
            '3': self.jnz,
            '4': self.bxc,
            '5': self.out,
            '6': self.bdv,
            '7': self.cdv,
        }
        return cmdmap[cmdcode]

    def printer(self):
        if self.debug:
            print(','.join(self.buffer))
        return self.buffer

    def run(self):
        ptr = 0
        while ptr < len(self.commands):
            command = self.get_cmd(self.commands[ptr])
            if self.debug:
                print(f'Running {command.__name__} with input {self.commands[ptr + 1]}. \
                        A:{bin(self.A)[2:]}, B:{bin(self.B)[2:]}, C:{bin(self.C)[2:]}')
            new_ptr = command(self.commands[ptr + 1])
            if isinstance(new_ptr, int):
                ptr = new_ptr
                if self.debug:
                    print('\n')
            else:
                ptr += 2

        return self.printer()

    # COMMANDS #
    def adv(self, operand):
        operand = self.get_combo_value(operand)
        self.A = math.floor(self.A / pow(2, operand))

    def bxl(self, operand):
        operand = int(operand)
        self.B = self.B ^ operand

    def bst(self, operand):
        operand = self.get_combo_value(operand)
        self.B = operand % 8

    def jnz(self, operand):
        operand = int(operand)
        if self.A:
            return operand

    def out(self, operand):
        operand = self.get_combo_value(operand)
        self.buffer.append(str(operand % 8))

    def bxc(self, operand):
        self.B = self.B ^ self.C

    def bdv(self, operand):
        operand = self.get_combo_value(operand)
        self.B = math.floor(self.A / pow(2, operand))

    def cdv(self, operand):
        operand = self.get_combo_value(operand)
        self.C = math.floor(self.A / pow(2, operand))


with open('inputs/2024/day17.txt', 'r') as file:
    real = file.read()

a, b, c, cmds = parse_text(real)


def solver(s, cmds, i):
    for num in range(8):
        num = format(num, '03b')
        snum = s + num + '0' * (48 - 3 * i)
        a = str(int(snum, 2))
        cmp = Compiler(a, b, c, cmds, debug=False)
        out = cmp.run()

        if out[-i] == cmds[-i]:
            if out == cmds:
                return a
            new_s = s + num
            solved = solver(new_s, cmds, i + 1)
            if solved:
                return solved
            else:
                continue

    else:
        return 0


a, b, c, cmds = parse_text(real)
cmp = Compiler(a, b, c, cmds, debug=False)
out = cmp.run()
print(out)

print(solver('', cmds, 1))
