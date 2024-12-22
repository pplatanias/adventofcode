def mhash(num):
    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216
    return num


def seq_runner(seq, solver_seq):
    diff_only = [x[1] for x in seq]
    w = len(solver_seq)
    slidings = [tuple(diff_only[i:i + w]) for i in range(0, len(diff_only) - w + 1)]
    for i in range(len(slidings)):
        if solver_seq == slidings[i]:
            return seq[i + w - 1][0], i
    else:
        return 0, 0


def find_uniq_sequences(seq):
    w = 4
    diff_only = [x[1] for x in seq]
    slidings = [tuple(diff_only[i:i + w]) for i in range(0, len(diff_only) - w + 1)]
    unique_slidings = set(slidings)
    return unique_slidings


def find_all_uniq_sequences(seqs):
    all_unique = set()
    for idx, seq in enumerate(seqs):
        new_uniques = find_uniq_sequences(seq)
        print(f'sequence {idx} had {len(new_uniques)} 4-length sequences')
        all_unique = all_unique.union(new_uniques)
    print(len(all_unique))
    return all_unique


with open('inputs/2024/day22.txt') as file:
    raw = [int(x) for x in file.read().split('\n')]

# Part 1
tot = 0
for num in raw:
    for i in range(2000):
        num = mhash(num)
    tot += num
print(tot)

# Part 2
seqs = []
for num in raw:
    seq = [(int(str(num)[-1]), 'X')]
    for i in range(2000):
        num = mhash(num)
        seq.append((int(str(num)[-1]), int(str(num)[-1]) - seq[-1][0]))
    seqs.append(seq)

uniq_seqs = find_all_uniq_sequences(seqs)

x_bananas = {}
for uniq_seq in uniq_seqs:
    bananas = 0
    for idseq, seq in enumerate(seqs):
        extra_bananas, i = seq_runner(seq, uniq_seq)
        bananas += extra_bananas

    print(f'uniq_seq {uniq_seq} found {bananas} total bananas')
    x_bananas[uniq_seq] = bananas

    # Let this run for a while and the max number you get here will be the solution. Ogre mode. I apologize.
    print(max(x_bananas.values()), max(x_bananas, key=x_bananas.get))
