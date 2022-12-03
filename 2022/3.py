import time
import string
start_time = time.time()

with open("3.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    data = [(line[:len(line)//2], line[len(line)//2:]) for line in lines]

value = 0
for (comp1, comp2) in data:
    double = set(comp1).intersection(set(comp2)).pop()
    if double.islower():
        value += string.ascii_lowercase.index(double) + 1
    else:
        value += string.ascii_uppercase.index(double) + 27

print(value)

value = 0
for i in range(0, len(lines), 3):
    triple = set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2])).pop()
    if triple.islower():
        value += string.ascii_lowercase.index(triple) + 1
    else:
        value += string.ascii_uppercase.index(triple) + 27

print(value)

print("--- %s seconds ---" % (time.time() - start_time))