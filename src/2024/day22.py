def mhash(num):
    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216
    return num


def find_sequences_and_prices(buyer_seqs):
    buyer_sequences_and_prices = []

    for buyer_seq in buyer_seqs:
        buyer_dict = {}
        slidings = [tuple(buyer_seq[i:i + 4]) for i in range(0, len(buyer_seq) - 4 + 1)]
        for sliding in slidings:
            sequence = tuple(x[1] for x in sliding)
            price = sliding[-1][0]
            if not buyer_dict.get(sequence):
                buyer_dict[sequence] = price
        buyer_sequences_and_prices.append(buyer_dict)
    return buyer_sequences_and_prices


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

buyer_dicts = find_sequences_and_prices(seqs)
all_seqs = set()
for buyer in buyer_dicts:
    all_seqs.update(tuple(buyer.keys()))

seq_and_bananas = {}
for seq in all_seqs:
    bananas = 0
    for buyer in buyer_dicts:
        bananas += buyer.get(seq, 0)
    seq_and_bananas[seq] = bananas
print(max(seq_and_bananas.values()))
