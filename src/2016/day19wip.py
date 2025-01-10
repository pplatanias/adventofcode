x = 3001330
#x = 42

curr = 1
step = 1
next_ = 2
print(x, curr, next_)
while x > 2:
    old_x = x
    step *= 2
    next_ = curr + step

    x = x//2

    if old_x % 2 == 0:
        pass
    else:
        curr = next_
    print(x, curr, next_)
print(curr)

# 100 : index18, elf19 // 512 : index294 elf295


def get_antidia(i,x,iters):
    real_len = len(x) - iters
    small_list = [idx for idx,z in enumerate(x) if z>0]

    real_i = small_list.index(i)
    starting_idx = (real_i+(real_len)//2) % real_len
    return small_list[starting_idx]


x = [1]*100
i = 0
iters = 0
while len([z for z in x if z>0]) > 1:
    if x[i] > 0:
        idx = get_antidia(i,x, iters)
        x[i] += x[idx]
        x[idx] = 0
        iters+=1

    i = (i + 1) % (len(x)-iters)
    print(i)
    print(x)


"""
0004060
0004060

111111111111111111....
202020202020202020....
2 2 2 2 2 2 2 2 2...
0 0 4 0 4 0 4 0 8...
    4   4   4   8...
    8   0   B   0...
    8       B...
    X


111111111111111111111111111111111111....
202020202020202020202020202020202020....
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ...
4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 0...
4   4   4   4   4   4   4   4   4...
0   0   8   0   8   0   8   0   B...
        8       8       8       B...
        F       0       F4      0
        F               F4
        FU


11111111111111111111....
20202020202020202020....
2 2 2 2 2 2 2 2 2 2 ...
4 0 4 0 4 0 4 0 4 0 ...
4   4   4   4   4...
0   0   4   0   B...
        4       B...
        X

111111111111111111111111111111111111111111....
202020202020202020202020202020202020202020....

2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ...
0 0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 ...

    4   4   4   4   4   4   4   4   4   4 ...
    8   0   8   0   8   0   8   0   8   0 ...

    8       8       8       8       8     ...
    0       0       F       0       FF    ...

                    F               FF    ...
                    FFF             0     ...

# 32
11111111111111111111111111111111.. curr 1 next 2  step 1
20202020202020202020202020202020.. curr 1 next 3  step 2

2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ..
4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 .. curr 1 next 5  step 4

4   4   4   4   4   4   4   4   ..
8   0   8   0   8   0   8   0   .. curr 1 next 9  step 8

8       8       8       8       ...
F       0       F       0       .. curr 1 next 17 step 16

F               F               ..
F               0               .. curr 1 next x


========================
01234  len 5  5//2 = 2
01234  len 5  5//2 = 2 . 3 + 2 mod 5 = 0

11111111111111111111
111111111 1111111111

111111111  111111111

111111111111111111

"""