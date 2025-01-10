from hashlib import md5
from multiprocessing import Pool, cpu_count

key = 'wtnhxymk'


def calc_md5(i, prefix='00000'):
    code = md5((key + str(i)).encode('utf-8')).hexdigest()
    if code.startswith(prefix):
        return (i, code)


if __name__ == "__main__":

    # Part 1
    tasks = range(30000000)
    with Pool(cpu_count()) as p:
        results = p.map(calc_md5, tasks)

    results = sorted([x for x in results if x is not None])

    pt1_results = results[0:8]
    print(''.join([x[1][5] for x in pt1_results]))

    # Part 2
    pwd = [0] * 8
    for i in range(len(pwd)):
        for result in results:
            if str(i) == result[1][5]:
                pwd[i] = result[1][6]
                break
    print(''.join(pwd))
