import os
import sys

with open(os.path.join(sys.path[0], "4.txt"), "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

rolls = lines.pop(0)
rolls = [int(x) for x in rolls.split(",")]

lines = list(filter(lambda s: s != "", lines))
boards = [[[int(x) for x in line] for line in board] for board in [[filter(lambda s: s != "", line) for line in board] for board in [[line.split(" ") for line in board] for board in [lines[n*5:(n+1)*5] for n in range(int(len(lines)/5))]]]]

won = False
winning = 0
last = 0

for i in range(len(rolls)):
    for index, board in enumerate(boards):
        for row in board:
            if sum(list([1 if x in rolls[:i+1] else 0 for x in row])) == 5:
                won = True
                winning = index
                last = i
                break
        for column in zip(*board):
            if sum(list([1 if x in rolls[:i+1] else 0 for x in column])) == 5:
                won = True
                winning = index
                last = i
                break
        if(won):
            break
    if(won):
        break

unmarked = sum(list([0 if x in rolls[:last+1] else x for line in boards[winning] for x in line]))

print(unmarked * rolls[last])

