import time
start_time = time.time()

with open("2.txt", "r") as file:
    lines = file.readlines()
    data = [line.strip().split(" ") for line in lines]

shape = {"X": 1, "Y": 2, "Z": 3}
beats = {"X": "C", "Y": "A", "Z": "B"}
equals = {"X": "A", "Y": "B", "Z": "C"}
points = 0
for (elve, me) in data:
    if elve == equals[me]:
        points += 3
        points += shape[me]
    elif beats[me] == elve:
        points += 6
        points += shape[me]
    else:
        points += shape[me]

print(points)

points = 0
equals_reversed = {"A": "X", "B": "Y", "C": "Z"}
beats = {"B": "X", "C": "Y", "A": "Z"}
for (elve, me) in data:
    if me == "Y":
        points += shape[equals_reversed[elve]]
        points += 3
    elif me == "X":
        points += shape[beats[elve]]
    else:
        points += shape[{"X", "Y", "Z"}.difference(set([equals_reversed[elve], beats[elve]])).pop()]
        points += 6

print(points)

print("--- %s seconds ---" % (time.time() - start_time))