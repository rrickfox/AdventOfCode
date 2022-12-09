import time
start_time = time.time()

with open("9.txt", "r") as file:
    lines = file.readlines()
    data = [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]

def move(direction):
    global hx, hy, tx, ty
    if direction == "U":
        hy += 1
    elif direction == "R":
        hx += 1
    elif direction == "D":
        hy -= 1
    else:
        hx -= 1
    moveTail((tx - hx, ty - hy))

def moveTail(relPos):
    global hx, hy, tx, ty
    if max(map(abs, relPos)) <= 1: return # no need to move if we are only 0 or 1 away at most
    if relPos[0] > 1 and abs(relPos[1]) <= 1:
        tx -= 1
        ty = hy
        return
    if relPos[0] < -1 and abs(relPos[1]) <= 1:
        tx += 1
        ty = hy
        return
    if relPos[1] > 1 and abs(relPos[0]) <= 1:
        ty -= 1
        tx = hx
        return
    if relPos[1] < -1 and abs(relPos[0]) <= 1:
        ty += 1
        tx = hx
        return
    print(f"====== wrong value: {relPos} ======")

# up and right are positive
hx = hy = 0
tx = ty = 0
visited = {(0, 0)}
for direction, count in data:
    for j in range(count):
        move(direction)
        visited.add((tx, ty))

print(len(visited))

print("--- %s seconds ---" % (time.time() - start_time))