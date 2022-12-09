import time
start_time = time.time()

with open("aoc09.txt", "r") as file:
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
    for i in range(len(tx)):
        if i == 0:
            tx[i], ty[i] = moveTail((tx[i] - hx, ty[i] - hy), (tx[i], ty[i]), (hx, hy))
        else:
            tx[i], ty[i] = moveTail((tx[i] - tx[i-1], ty[i] - ty[i-1]), (tx[i], ty[i]), (tx[i-1], ty[i-1]))
    # moveTail((tx - hx, ty - hy))

def moveTail(relPos, current, previous):
    # print(relPos)
    tx, ty = current
    hx, hy = previous
    if max(map(abs, relPos)) <= 1: return current # no need to move if we are only 0 or 1 away at most
    if relPos[0] > 1 and abs(relPos[1]) <= 1: # right side
        tx -= 1
        ty = hy
    elif relPos[0] < -1 and abs(relPos[1]) <= 1: # left side
        tx += 1
        ty = hy
    elif relPos[1] > 1 and abs(relPos[0]) <= 1: # up
        ty -= 1
        tx = hx
    elif relPos[1] < -1 and abs(relPos[0]) <= 1: # down
        ty += 1
        tx = hx
    elif relPos[0] > 1 and relPos[1] > 1: # top-right-corner
        tx -= 1
        ty -= 1
    elif relPos[0] < -1 and relPos[1] < -1: # bottom-left-corner
        tx += 1
        ty += 1
    elif relPos[0] > 1 and relPos[1] < -1: # bottom-right
        tx -= 1
        ty += 1
    elif relPos[0] < -1 and relPos[1] > 1: # top-left
        tx += 1
        ty -= 1
    else:
        print(f"====== wrong value: {relPos} ======")
    return tx, ty

# up and right are positive
hx = hy = 0
tx = [0 for _ in range(9)]
ty = [0 for _ in range(9)]
visited = {(0, 0)}
for direction, count in data:
    for _ in range(count):
        move(direction)
        # print(f"H: {(hx, hy)}, T: {list(zip(tx, ty))}")
        visited.add((tx[-1], ty[-1]))

print(len(visited))

print("--- %s seconds ---" % (time.time() - start_time))