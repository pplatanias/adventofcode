import re

with open('inputs/2016/day09.txt', 'r') as file:
    entire = file.read()

def get_decompress_len(string, recurse=True):
    totalsize = 0
    i = 0
    while i < len(string):
        if string[i] == '(':
            close = string[i:].find(')') + i
            forward,repeat = string[i+1:close].split('x')
            i = close + int(forward) + 1
            if recurse:
                totalsize += (int(repeat)) * get_decompress_len(string[close+1:i], recurse=recurse)
            else:
                totalsize += (int(repeat)) * len(string[close+1:i])
        else:
            i+=1
            totalsize += 1
    return totalsize

print(get_decompress_len(entire, recurse=False))
print(get_decompress_len(entire, recurse=True))
