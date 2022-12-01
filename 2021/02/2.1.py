filename = r"D:\data\Richard\!Studium\Dresden\3. Semester\AdventOfCode\02\2.txt"

with open(filename, "r") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

inst = []

for line in lines:
    inst.append(line.split(" "))

x = 0
depth = 0

for i in inst:
    if i[0] == "forward":
        x += int(i[1])
    elif i[0] == "up":
        depth -= int(i[1])
    elif i[0] == "down":
        depth += int(i[1])

print(x * depth)