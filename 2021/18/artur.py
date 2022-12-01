from time import time
from functools import reduce as funcreduce
from itertools import permutations
import sys
start = time()
data = open("18.txt").read().replace(',', ", ").split('\n')

# ======== code =======

def magnitude(n):
    if type(n) == int: return n
    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])

def convert(n: str) -> list:
    if n.isdigit(): return int(n)
    x = 0
    for i in range(1, len(n)):
        x += (n[i] == '[') - (n[i] == ']')
        if n[i] == ',' and not x:
            return [convert(n[1:i]), convert(n[i + 2:-1])]

def unwind(n) -> list:
    if type(n) == int: return [n]
    return ['['] + unwind(n[0]) + [', '] + unwind(n[1]) + [']']

def explode(n: list) -> list:
    i = x = 0
    while i < len(n) - 1:
        x += (n[i] == '[') - (n[i] == ']')
        if x > 4 and n[i] + n[i + 2] + n[i + 4] == "[, ]":
            # print(''.join([str(x) for x in n])) # lalalalalalala
            i0, i1, n0, n1 = i, i + 1, n[i + 1], n[i + 3]
            n = n[:i] + [0] + n[i + 5:]
            i = x = 0
            while i0 > 0: 
                i0 -= 1
                if type(n[i0]) == int: n[i0] += n0; break
            while i1 < len(n) - 1: 
                i1 += 1
                if type(n[i1]) == int: n[i1] += n1; break
        else: i += 1
    return n

def reduce(n: list) -> list:
    n = explode(n)
    i = 0
    while i < len(n) - 1:
        if type(n[i]) == int and n[i] > 9:
            # print(''.join([str(x) for x in n])) # lalalalalala
            n = explode(n[:i] + unwind([n[i] // 2, n[i] // 2 + n[i] % 2]) + n[i + 1:])
            i = 0
        else: i += 1
    return convert(''.join([str(x) for x in n]))

data = [convert(line) for line in data]
print(magnitude(funcreduce(lambda x, y: reduce(unwind([x, y])), data)))
print(max([magnitude(reduce(unwind([x, y]))) for (x, y) in permutations(data, 2)]))

print(f"\n===== {time() - start} sec =====")