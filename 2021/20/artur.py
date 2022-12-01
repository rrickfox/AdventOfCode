from time import time
from itertools import product
import sys
start = time()
data = open("20.txt").read().replace('#', '1').replace('.', '0').split('\n\n')

# ======== code =======

def run(data, outside):
    return [''.join([lookup[int(''.join([data[y + j][x + i] if 0 <= x + i < len(data[0]) and 0 <= y + j < len(data) else outside for (j, i) in product([-1, 0, 1], [-1, 0, 1])]), 2)] for x in range(-1, len(data[0]) + 1)]) for y in range(-1, len(data) + 1)], lookup[int(9 * outside, 2)]

lookup, data, outside = data[0], data[1].split('\n'), '0'
print(''.join(run(*run(data, outside))[0]).count('1'))
for i in range(50):
    data, outside = run(data, outside)
print(''.join(data).count('1'))

print(f"\n===== {time() - start} sec =====")