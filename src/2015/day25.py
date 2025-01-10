y = 2981
x = 3075


def find_code_id(y, x):
    row = y + x - 1
    row_0 = ((row * (row - 1)) // 2)
    return row_0 + x


def find_code(idx):
    s = 20151125
    for i in range(idx - 1):
        s *= 252533
        s = divmod(s, 33554393)[1]
    return s


print(find_code(find_code_id(y, x)))
