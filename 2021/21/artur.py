from time import time
from itertools import product
import sys
start = time()
data = open("21.txt").read().split('\n')

# ======== code =======

def part1(p0, p1):
    die = 1
    s0 = s1 = 0
    while True:
        p0 = (p0 + 3 * ((die - 1) % 100 + 1) + 3 -1) % 10 + 1
        s0 += p0
        die += 3
        if s0 >= 1000: return s1 * (die - 1)
        p1 = (p1 + 3 * ((die - 1) % 100 + 1) + 3 -1) % 10 + 1
        s1 += p1
        die += 3
        if s1 >= 1000: return s0 * (die - 1)

def part2(p0, p1):
    won0 = won1 = 0
    universes = {(0, 0, p0, p1): 1}
    turn = True
    while len(universes):
        new_universes = {}
        for universe in universes:
            s0, s1, p0, p1 = universe
            if turn:
                for die in product([1, 2, 3, 4, 5, 6], repeat=3):
                    p = (p0 + sum(die) - 1) % 10 + 1
                    if s0 + p >= 21: won0 += universes[universe]
                    else:
                        new = (s0 + p, s1, p, p1)
                        new_universes[new] = new_universes.get(new, 0) + universes[universe]
            else:
                for die in product([1, 2, 3, 4, 5, 6], repeat=3):
                    p = (p1 + sum(die) - 1) % 10 + 1
                    if s1 + p >= 21: won1 += universes[universe]
                    else:
                        new = (s0 , s1 + p, p0, p)
                        new_universes[new] = new_universes.get(new, 0) + universes[universe]
        universes = new_universes
        turn = not turn
    return max(won0, won1)

p0, p1 = int(data[0][-1]), int(data[1][-1])
print(part1(p0, p1))
print(part2(p0, p1))

print(f"\n===== {time() - start} sec =====")