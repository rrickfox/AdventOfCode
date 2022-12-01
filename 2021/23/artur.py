from time import time
import sys
from copy import deepcopy
from cache import selective_cache
start = time()
data = open("23.txt").read().split('\n')

# ======== code =======

@selective_cache("floor", "rooms", "value")
def run(floor, rooms, value, n):
    global mv
    if sum(sum(x == i for x in rooms[i]) for i in range(4)) == 4 * n: mv = value
    for f, x in enumerate(floor):
        if x == None: continue
        mn, mx = min(f, 2 * x + 2), max(f, 2 * x + 2)
        if sum(1 for i in range(mn, mx + 1) if floor[i] != None) == 1 and rooms[x][0] == None:
            tfloor = deepcopy(floor)
            tfloor = tfloor[:f] + (None,) + tfloor[f + 1:]
            for i in range(n)[::-1]:
                if rooms[x][i] == None:
                    trooms = deepcopy(rooms)
                    trooms = trooms[:x] + (trooms[x][:i] + (x,) + trooms[x][i + 1:],) + trooms[x + 1:]
                    v = value + (mx - mn + i + 1) * pow(10, x)
                    if v < mv: run(tfloor, trooms, v, n)
                    break
                if rooms[x][i] != x: break

    for r in range(4):
        room = [x for x in rooms[r] if x != None]
        if not room or sum(x == r for x in room) == len(room): continue
        x, i = room[0], n - len(room)
        mn = mx = r * 2 + 2
        while mn > 0 and floor[mn - 1] == None: mn -= 1
        while mx < 10 and floor[mx + 1] == None: mx += 1
        trooms = deepcopy(rooms)
        trooms = trooms[:r] + (trooms[r][:i] + (None,) + trooms[r][i + 1:],) + trooms[r + 1:]
        for f in set(range(mn, mx + 1)) & {0, 1, 3, 5, 7, 9, 10}:
            tfloor = deepcopy(floor)
            tfloor = tfloor[:f] + (x,) + tfloor[f + 1:]
            v = value + (abs(r * 2 + 2 - f) + i + 1) * pow(10, x)
            if v < mv: run(tfloor, trooms, v, n)

floor = tuple(None for _ in range(11))
rooms = tuple(tuple(ord(data[j][i]) - 65 for j in [2, 3]) for i in [3, 5, 7, 9])
# ((1, 0), (2, 3), (1, 2), (3, 0)) -> log10(value) + index of room
mv = float('inf')
run(floor, rooms, 0, 2)
print(mv)

mv = float('inf')
data = data[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + data[3:]
rooms = tuple(tuple(ord(data[j][i]) - 65 for j in [2, 3, 4, 5]) for i in [3, 5, 7, 9])
run(floor, rooms, 0, 4)
print(mv)

print(f"\n===== {time() - start} sec =====")
