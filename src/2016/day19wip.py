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




#x = [1] * 3001330 + 1
#x = list(range(1,101))
x = list(range(1,6+1))
print(f'start: {x}')
import time
now = time.time()
while len(x) > 1:
    i = 0
    old_idx = 0
    for idx in range(len(x)):
        if x[idx] != 0:
            #x[idx] += x[((len(x))//2)+i]
            x[(((len(x)-i)//2)+i+idx) % (len(x))] = 0
            i+=1
        else:
            break
        print(x)
        old_idx = idx
    cursor = x[old_idx]
    x = [z for z in x if z > 0]
    cursor = x.index(cursor)
    x = x[cursor+1:] + x[:cursor+1]
    print('cut zeros and rotate to cursor=', x)


print(x)
print(f'{time.time()-now}')