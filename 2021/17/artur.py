from time import time
start = time()
data = open("17.txt").readline()

# ======== code =======

oys = {}

def run(xs, ys, high=False):
    ox = xs
    oy = ys
    steps = 0
    x = y = 0
    if high: ym = 0
    while True:
        steps += 1
        x += xs
        y += ys
        if high and y > ym: ym = y
        xs += -1 if xs > 0 else xs != 0
        ys -= 1
        if x0 <= x <= x1 and y0 <= y <= y1:
            if high:
                return ym
            else:
                print(str(oy) + " " + str(steps))
                oys[oy] = oys.get(oy, set()).union({ox})
                return True
        if y < y0 or x > x1: return False

def find(xm, ym, high=False):
    velocitys = 0
    for ys in range(-ym, ym)[::-1]:
        for xs in range(-xm, xm):
            if run(xs, ys, high): 
                if high: 
                    return run(xs, ys, high) 
                else: 
                    velocitys += 1
    return velocitys

(x0, x1), (y0, y1) = ((int(x[x.index('=') + 1:x.index("..")]), int(x[x.index("..") + 2:])) for x in data.split(', '))

print(find(18, 150, True))
print(find(200, 200))
print(oys)
for y in range(min(oys.keys()), max(oys.keys())+1):
    if y in oys:
        print(str(y) + ": " + str(sorted(list(oys[y]))))

print(f"\n===== {time() - start} sec =====")