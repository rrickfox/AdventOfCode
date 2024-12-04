import time
from collections import defaultdict

start_time = time.time()

with open("04.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

num = 0
num += sum(sum(1 if str(line[i:]).startswith("XMAS") else 0 for i in range(0, len(line))) for line in data)
num += sum(sum(1 if str(line[i:]).startswith("SAMX") else 0 for i in range(0, len(line))) for line in data)
num += sum(sum(1 if "".join(col[i:]).startswith("XMAS") else 0 for i in range(0, len(data))) for col in zip(*data))
num += sum(sum(1 if "".join(col[i:]).startswith("SAMX") else 0 for i in range(0, len(data))) for col in zip(*data))

# https://stackoverflow.com/a/43311126/8990620
def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

fdiag = groups(data, lambda x, y: x + y)
bdiag = groups(data, lambda x, y: x - y)

num += sum(sum(1 if "".join(line[i:]).startswith("XMAS") else 0 for i in range(0, len(line))) for line in fdiag)
num += sum(sum(1 if "".join(line[i:]).startswith("SAMX") else 0 for i in range(0, len(line))) for line in fdiag)
num += sum(sum(1 if "".join(line[i:]).startswith("XMAS") else 0 for i in range(0, len(line))) for line in bdiag)
num += sum(sum(1 if "".join(line[i:]).startswith("SAMX") else 0 for i in range(0, len(line))) for line in bdiag)
print(num)

def groups_with_pos(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append((data[y][x], x, y))
    return list(map(grouping.get, sorted(grouping)))

middle_pos_forward = [[(diag[i+1][1], diag[i+1][2]) for i in range(0, len(diag)) if "".join(tup[0] for tup in diag[i:]).startswith("MAS") or "".join(tup[0] for tup in diag[i:]).startswith("SAM")] for diag in groups_with_pos(data, lambda x, y: x + y)]
middle_pos_backward = [[(diag[i+1][1], diag[i+1][2]) for i in range(0, len(diag)) if "".join(tup[0] for tup in diag[i:]).startswith("MAS") or "".join(tup[0] for tup in diag[i:]).startswith("SAM")] for diag in groups_with_pos(data, lambda x, y: x - y)]
s1 = {(x, y) for diag in middle_pos_forward for x, y, in diag}
s2 = {(x, y) for diag in middle_pos_backward for x, y, in diag}
print(len(s1.intersection(s2)))

print(f"--- {(time.time() - start_time)} seconds ---")