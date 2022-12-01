filename = r"D:\data\Richard\!Studium\Dresden\3. Semester\AdventOfCode\01\1.txt"

with open(filename, "r") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

counter = 0

sums = []

for i, j in enumerate(lines[:-2]):
    sums.append(int(j) + int(lines[i+1]) + int(lines[i+2]))

for i, j in enumerate(sums[:-1]):
    if int(j) < int(sums[i+1]):
        counter = counter + 1

print(counter)