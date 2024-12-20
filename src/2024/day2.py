with open('inputs/2024/day2.txt', 'r') as file:
    reports = [x for x in file.read().split('\n')]

good = 0
for report in reports:
    report = [int(x) for x in report.split()]
    if (all((abs(x - y) <= 3 and x != y) for x, y in zip(report[:-1], report[1:]))
            and (sorted(report) == report or sorted(report, reverse=True) == report)):
        good += 1
print(good)

good = 0
for report in reports:
    report = [int(x) for x in report.split()]
    if (all((abs(x - y) <= 3 and x != y) for x, y in zip(report[:-1], report[1:]))
            and (sorted(report) == report or sorted(report, reverse=True) == report)):
        good += 1
    else:
        for x in range(len(report)):
            new_report = list(report)
            new_report.pop(x)
            if (all((abs(x - y) <= 3 and x != y) for x, y in zip(new_report[:-1], new_report[1:]))
                    and (sorted(new_report) == new_report or sorted(new_report, reverse=True) == new_report)):
                good += 1
                break
print(good)
