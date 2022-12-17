import time, math
from itertools import cycle
start_time = time.time()

with open("17.txt", "r") as file:
    data = list(file.read().strip())

#############################
# Part 1 is simulated
# for part 2 I printed a list of tuples, containing the ID of the block placed and the x position of it at rest
# I copied it into my editor and tried to find a repetition
# this is different for every input and even the example
# this affects the variables first, between, height and h
# first and between mean the nth block placed
# I found them by looking for the beginning of my cycle at the end of the calc() function
# eg if the id is 2 and the position is 2 print i
# then look for the 19th time that occurred because that is the start of the first repetition in my input
# repeat this for the first time it starts again
# look into 17_cycles for this, turn off word wrap, line 5 and 6 are exactly the same

class Block:
    def __init__(self, width: int, ident: int, points):
        self.width = width
        self.ident = ident
        self.points = points
        self.pos = 2

    def reset(self):
        self.pos = 2

blocks = cycle([
    Block(4, 0, [(0, 0), (1, 0), (2, 0), (3, 0)]),
    Block(3, 1, [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]),
    Block(3, 2, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
    Block(1, 3, [(0, 0), (0, 1), (0, 2), (0, 3)]),
    Block(2, 4, [(0, 0), (1, 0), (0, 1), (1, 1)])])

directions = cycle(data)

room = [{-1}, {-1}, {-1}, {-1}, {-1}, {-1}, {-1}]

def get_xy(x, y):
    global room
    return y in room[x]

def set_xy(x, y):
    global room
    room[x].add(y)

def print_room():
    ymax = max(max(s) for s in room)
    for y in range(ymax, -1, -1):
        print("|", end="")
        for x in range(7):
            print("#" if get_xy(x, y) else ".", end="")
        print("|")
    print("|-------|")
    print()

# time until beginning of repetition
first = 247
# number of blocks between repetition
between = 1755
# height gained per repetition
height = 2747
r = None

def calc(i, part1):
    global blocks, directions, first, between, room, r
    block = next(blocks)
    block.reset()
    y = max(max(s) for s in room) + 4
    # move horizontally and down alternately
    for d in cycle(["lr", "down"]):
        if d == "down":
            # if any point of the current block will collide with an already placed one, this block is finished
            if any(get_xy(point[0] + block.pos, point[1] + y - 1) for point in block.points):
                break
            else:
                y -= 1
        else:
            lr = next(directions)
            if lr == "<":
                # move left only if it will not collide with the wall and no point will collide an already placed one
                if block.pos >= 1 and not any(get_xy(point[0] + block.pos - 1, point[1] + y) for point in block.points):
                    block.pos -= 1
            else:
                # analoge to moving left
                if block.pos <= 6 - block.width and not any(get_xy(point[0] + block.pos + 1, point[1] + y) for point in block.points):
                    block.pos += 1
    # set the points
    for point in block.points:
        set_xy(block.pos + point[0], y + point[1])

    # part 2: when cycle starts, remember the way the blocks lie
    if (i - first) % between == 0 and part1:
        m = max(max(s) for s in room)
        r = [{t - m + 50 for t in s if m - t < 50} for s in room]

for i in range(2022):
    calc(i, True)

print(max(max(s) for s in room) + 1)

# height := height_until_first + height * repetitions + height_after_last
h = 371
remaining = 1000000000000 - first
h += height * math.floor(remaining / between)
remaining = 1000000000000 - first - between * math.floor(remaining / between)

# reset blocks and directions
blocks = cycle([
    Block(4, 0, [(0, 0), (1, 0), (2, 0), (3, 0)]),
    Block(3, 1, [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]),
    Block(3, 2, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
    Block(1, 3, [(0, 0), (0, 1), (0, 2), (0, 3)]),
    Block(2, 4, [(0, 0), (1, 0), (0, 1), (1, 1)])])
directions = cycle(data)

# move blocks and directions along until start of repetition
for i in range(first):
    calc(i, False)

# room, blocks and directions are now exactly the same as at beginning of repetition
room = r
for i in range(remaining):
    calc(i, False)

h += max(max(s) for s in room) - 50 + 1
print(h)

print("--- %s seconds ---" % (time.time() - start_time))