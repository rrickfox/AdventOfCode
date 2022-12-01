with open("1.txt") as file:
    data = file.readline()

s = 0

for i, digit in enumerate(data):
    n = i + (len(data) / 2)
    n = n - len(data) if n > len(data) - 1 else n
    if digit == data[int(n)]:
        s += int(digit)

print(s)