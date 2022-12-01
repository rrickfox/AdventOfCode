filename = r"D:\data\Richard\!Studium\Dresden\3. Semester\AdventOfCode\01\1.txt"

with open(filename, "r") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]



counter = 0

for i, j in enumerate(lines[:-1]):
    if int(j) < int(lines[i+1]):
        counter = counter + 1

print(counter)