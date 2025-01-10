elfcount = 3001330

def solve_1(elfcount):
    curr = 1        # Current leftmost elf
    step = 1        # Every iteration, middle elves disappear
    next_ = 2       # Current next elf from the leftmost
    print(elfcount, curr, next_)
    while elfcount > 2:

        # On every round, the distance between elves increases
        old_x = elfcount
        step *= 2
        next_ = curr + step

        elfcount = elfcount//2

        # Only on odd rounds, the leftmost is absorbed by the rightmost,
        # so the next leftmost is "next_"
        if old_x % 2 != 0:
            curr = next_
        print(elfcount, curr, next_)
    return curr

def solve_2(elfcount):
    x = list(range(1,elfcount+1))
    print(f'start: {x}')
    while len(x) > 1:
        i = 0
        old_idx = 0
        for idx in range(len(x)):
            if x[idx] != 0:
                # The magic formula
                x[(((len(x)-i)//2)+i+idx) % (len(x))] = 0
                i+=1
            else:
                # We stop on the first 0 to prune the list
                # otherwise the formula doesnt(?) work
                break
            print(x)
            # Save the last elf we processed
            old_idx = idx

        last_elf = x[old_idx]
        x = [z for z in x if z > 0]
        index_of_last_elf = x.index(last_elf)
        x = x[index_of_last_elf+1:] + x[:index_of_last_elf+1]
        print('cut zeros and rotate to cursor=', x)

    return x[0]

print(solve_1(elfcount))
#print(solve_2(elfcount))
print(solve_2(6))
