data = 265149

# This does not work

corners = {}

a = 0
increment = 1
cornerType = 0
corners[a] = cornerType
while a <= data:
    a += increment
    cornerType = (cornerType + 1) % 4
    corners[a] = cornerType
    a += increment
    cornerType = (cornerType + 1) % 4
    corners[a] = cornerType
    increment += 1

last_corner = max(corners.keys())
if corners[last_corner] == 2:
    count = sum([1 if val == 1 else 0 for val in corners.values()])
    dist = data - sorted(list(corners.keys()))[-2]
    print(count)
    print(sorted(list(corners.keys()))[-2])
    print(data)
    print(count * 2 - dist + 1)
else:
    print("Not Implemented ^^")
