from time import time
import sys
start = time()
data = open("24.txt").read().split('\n')

# ======== code =======

def step(z, w, a, b, c):
    x = z % 26 + b
    z //= a
    if x != w: 
        z *= 26
        z += w + c
    return z


def run(data, part2=False):
    zdict = {0: 0}
    for (a, b, c) in data:
        nzdict = {}
        for z in zdict:
            for w in range(1, 10):
                x = step(z, w, a, b, c)
                nzdict[x] = min(nzdict.get(x, float('inf')), zdict[z] * 10 + w) if part2 else max(nzdict.get(x, 0), zdict[z] * 10 + w)
        zdict = nzdict
        print(len(zdict))
    return zdict.get(0, None)

data = [(int(data[i + 4][6:]), int(data[i + 5][6:]), int(data[i + 15][6:])) for i in range(0, len(data), 18)]
print(run(data))
print(run(data, True))

print(f"\n===== {time() - start} sec =====")