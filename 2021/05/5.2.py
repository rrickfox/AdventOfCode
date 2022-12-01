import os, sys

with open(os.path.join(sys.path[0], "5.txt"), "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

lines = [[(int(line[0]), int(line[1].split(" -> ")[0])), (int(line[1].split(" -> ")[1]), int(line[2]))] for line in [line.split(",") for line in lines]]
non_diag = list(filter(lambda line: (line[0][0] == line[1][0] or line[0][1] == line[1][1]), lines))

max_count = max(max(map(max, lines)))

board = [[0 for j in range(max_count + 1)] for i in range(max_count + 1)]

for line in non_diag:
    startX = min(line[0][0], line[1][0])
    endX = max(line[0][0], line[1][0])
    startY = min(line[0][1], line[1][1])
    endY = max(line[0][1], line[1][1])
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            board[x][y] += 1

diag = list(filter(lambda line: (abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1])), lines))
print(diag)

for line in diag:
    offset = abs(line[0][0] - line[1][0])
    multX = 1 if line[0][0] < line[1][0] else -1
    multY = 1 if line[0][1] < line[1][1] else -1
    for i in range(0, offset + 1):
        board[line[0][0] + i * multX][line[0][1] + i * multY] += 1

out = sum([sum([1 if x >= 2 else 0 for x in line]) for line in board])

print(out)