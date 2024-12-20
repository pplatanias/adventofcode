class Disk:

    def __init__(self, inputstr):
        self.blocks = []
        self.bblocks = []
        fileidx = 0
        cursor = 0
        for idx, ch in enumerate(inputstr):
            if not idx % 2:  # if isfile
                self.blocks.extend([str(fileidx)] * int(ch))
                self.bblocks.append([cursor, cursor + int(ch) - 1, fileidx])
                fileidx += 1
                cursor += int(ch)
            else:
                self.blocks.extend(['.'] * int(ch))
                self.bblocks.append([cursor, cursor + int(ch) - 1, -1])
                cursor += int(ch)

    def defrag(self):
        self.new_blocks = ['x'] * len(self.blocks)
        for idx, block in enumerate(self.blocks):
            if block == '.':
                for tailidx, lookblock in enumerate(self.blocks[:idx:-1]):
                    if lookblock != '.' and lookblock != 'X':
                        self.new_blocks[idx] = lookblock
                        self.blocks[-1 - tailidx] = '.'
                        break
                else:
                    self.new_blocks[idx] = '.'
            else:
                self.new_blocks[idx] = block
        self.blocks = self.new_blocks

    def defrag2(self):
        for lookblock in self.bblocks[::-1]:
            if lookblock[2] >= 0:
                lwidth = lookblock[1] - lookblock[0] + 1

                for block in self.bblocks:

                    if block[0] < lookblock[0] and block[2] < 0:
                        width = block[1] - block[0] + 1

                        if lwidth <= width:
                            lookblock[0] = block[0]
                            lookblock[1] = lookblock[0] + lwidth - 1
                            block[0] = block[0] + lwidth
                            break

    def get_chk(self):
        sum = 0
        for idx, ch in enumerate(self.blocks):
            if ch != '.':
                sum += idx * int(ch)
        return sum

    def get_chk2(self):
        sum = 0
        for block in self.bblocks:
            if block[2] > 0:
                idxes = range(block[0], block[1] + 1)
                for idx in idxes:
                    sum += idx * int(block[2])
        return sum

    def __repr__(self):
        return 'Disk<' + ''.join(self.blocks) + '>'

    def __str__(self):
        return ''.join(self.blocks)


with open('inputs/2024/day9.txt', 'r') as file:
    inp = file.read()

d = Disk(inp)
d.defrag()
print(d.get_chk())

d = Disk(inp)
d.defrag2()
print(d.get_chk2())
