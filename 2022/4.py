import time
start_time = time.time()

with open("4.txt", "r") as file:
    lines = [line.strip().split(",") for line in file.readlines()]
    data = [[list(map(int, x.split("-"))) for x in line] for line in lines]

value1 = 0
value2 = 0
for (elve1, elve2) in data:
    if (elve1[0] <= elve2[0] and elve1[1] >= elve2[1]) or (elve2[0] <= elve1[0] and elve2[1] >= elve1[1]):
        value1 += 1
    # if (elve1[0] >= elve2[0] and elve1[0] <= elve2[1]) or(elve1[1] >= elve2[0] and elve1[1] <= elve2[1]) or (elve2[0] >= elve1[0] and elve2[0] <= elve1[1]) or(elve2[1] >= elve1[0] and elve2[1] <= elve1[1]):
    if elve1[1] >= elve2[0] and elve2[1] >= elve1[0]:
        value2 += 1

print(value1)
print(value2)

print("--- %s seconds ---" % (time.time() - start_time))