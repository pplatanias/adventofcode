from collections import defaultdict
from itertools import combinations, permutations


def get_all(raw):
    points = defaultdict(list)
    for idy, row in enumerate(raw.split('\n')):
        for idx, char in enumerate(row):
            if char != '.':
                points[char].append((idy, idx))
    return points  # {'0': [(1, 8), (2, 5), (3, 7), (4, 4)], 'a': [(5, 6), (8, 8), (9, 9)]}


def find_verteces_of_two_points(a, b):
    c1 = ((2 * a[0] - b[0]), (2 * a[1] - b[1]))
    c2 = ((2 * b[0] - a[0]), (2 * b[1] - a[1]))
    return [c1, c2]


def find_all_verteces_for_freq(points):
    pairs = combinations(points, 2)
    new_pairs = []
    for pair in pairs:
        new_pairs.extend(find_verteces_of_two_points(pair[0], pair[1]))
    return new_pairs


def find_points_in_line(a, b, max_y, max_x):
    new_points = []

    vector = (b[0] - a[0], b[1] - a[1])
    y = a[0]
    x = a[1]
    while True:
        y = y + vector[0]
        x = x + vector[1]
        if y < max_y and x < max_x and y >= 0 and x >= 0:
            new_points.append((y, x))
        else:
            break

    return new_points


def get_all_linepoints_for_freq(points, max_y, max_x):
    pairs = permutations(points, 2)
    new_pairs = []
    for pair in pairs:
        new_pairs.extend(find_points_in_line(pair[0], pair[1], max_y, max_x))
    return new_pairs


def solve_1(input):
    max_y = len(input.split('\n'))
    max_x = len(input.split('\n')[0])
    freqs = get_all(input)
    total_new_points = set()

    for freq, pairs in freqs.items():
        new_points = find_all_verteces_for_freq(pairs)
        for new_p in new_points:
            if new_p[0] < max_y and new_p[1] < max_x and new_p[1] >= 0 and new_p[0] >= 0:
                total_new_points.add(new_p)

    return len(total_new_points)


def solve_2(input):
    max_y = len(input.split('\n'))
    max_x = len(input.split('\n')[0])
    freqs = get_all(input)
    total_new_points = set()

    for freq, pairs in freqs.items():
        new_points = get_all_linepoints_for_freq(pairs, max_y, max_x)
        for new_p in new_points:
            if new_p[0] < max_y and new_p[1] < max_x and new_p[1] >= 0 and new_p[0] >= 0:
                total_new_points.add(new_p)

    return len(total_new_points)


with open('inputs/2024/day8.txt', 'r') as file:
    real_input = file.read()

print(solve_1(real_input))
print(solve_2(real_input))
