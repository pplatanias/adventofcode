from hashlib import md5
from multiprocessing import Pool, cpu_count

with open('inputs/2015/day4.txt') as file:
    key = file.read()


def calc_md5(i, prefix='000000'):
    code = md5((key + str(i)).encode('utf-8')).hexdigest()
    if code.startswith(prefix):
        print(i)
        return 1


if __name__ == "__main__":

    for i in range(1000000):
        if calc_md5(i, prefix='00000'):
            break

    # Ogre mode
    tasks = range(10000000)
    with Pool(cpu_count()) as p:
        p.map(calc_md5, tasks)
