import heapq
import time

t_start = time.time()

with open("15.txt") as f:
    grid = [list(map(int, line.strip())) for line in f]

for EXPAND in [1, 5]:

    rows = len(grid)
    cols = len(grid[0])

    def truegrid(x, y):
        shifts = x // cols +  y // rows
        return (grid[x % cols][y % rows] + shifts - 1) % 9 + 1

    truecols = cols * EXPAND
    truerows = rows * EXPAND

    vis = [[False for _ in range(truecols)] for _ in range(truerows)]

    q = [(0, 0, 0)]
    vis[0][0] = True

    while q:

        d, x, y = heapq.heappop(q)

        if x == truecols-1 and y == truerows-1:
            print(f"Found minimum distance for EXPAND={EXPAND}: {d}")
            break

        if x > 0 and (not vis[x-1][y]):
            vis[x-1][y] = True
            heapq.heappush(q, (d+truegrid(x-1, y), x-1, y))

        if x+1 < truecols and (not vis[x+1][y]):
            vis[x+1][y] = True
            heapq.heappush(q, (d+truegrid(x+1, y), x+1, y))

        if y > 0 and (not vis[x][y-1]):
            vis[x][y-1] = True
            heapq.heappush(q, (d+truegrid(x, y-1), x, y-1))

        if y+1 < truerows and (not vis[x][y+1]):
            vis[x][y+1] = True
            heapq.heappush(q, (d+truegrid(x, y+1), x, y+1))

print(f"Took {time.time() - t_start} seconds")