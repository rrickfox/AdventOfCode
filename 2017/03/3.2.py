import time
start_time = time.time()
with open("3.txt") as file:
    data = int(file.readline())

corners = {}

a = 0
increment = 1
cornerType = 0
corners[a] = cornerType
while a <= 100:
    a += increment
    cornerType = (cornerType + 1) % 4
    corners[a] = cornerType
    a += increment
    cornerType = (cornerType + 1) % 4
    corners[a] = cornerType
    increment += 1

def neighbours(i):
    if i in corners.keys():
        same_corners = [x for x in corners.keys() if corners[x] == corners[i]]
        slc = same_corners[same_corners.index(i) - 1]
        snc = same_corners[same_corners.index(i) + 1]
        return (i + 1, i - 1, slc, snc, snc + 1, snc - 1, snc + 2, snc - 2)
    elif (i + 1) in corners.keys():
        same_corners = [x for x in corners.keys() if corners[x] == corners[i + 1]]
        slc = same_corners[same_corners.index(i + 1) - 1]
        snc = same_corners[same_corners.index(i + 1) + 1]
        return (i + 1, i + 2, i - 1, slc, slc - 1, snc - 1, snc - 2, snc - 3)
    elif (i - 1) in corners.keys():
        same_corners = [x for x in corners.keys() if corners[x] == corners[i - 1]]
        slc = same_corners[same_corners.index(i - 1) - 1]
        snc = same_corners[same_corners.index(i - 1) + 1]
        return (i - 1, i - 2, i + 1, slc, slc + 1, snc + 1, snc + 2, snc + 3)
    else:
        dist_to_corners = [abs(x - i) for x in sorted(list(corners.keys()))]
        nearest_corner = sorted(list(corners.keys()))[dist_to_corners.index(min(dist_to_corners))]
        same_corners = [x for x in corners.keys() if corners[x] == corners[nearest_corner]]
        slc = same_corners[same_corners.index(nearest_corner) - 1]
        snc = same_corners[same_corners.index(nearest_corner) + 1]
        if nearest_corner > i:
            dist = nearest_corner - i
            return (i + 1, i - 1, slc - dist + 1, slc - dist, slc - dist + 2, snc - dist - 1, snc - dist, snc - dist - 2)
        else:
            dist = i - nearest_corner
            return (i + 1, i - 1, slc + dist - 1, slc + dist - 2, slc + dist, snc + dist, snc + dist + 1, snc + dist + 2)


l = [1, 1, 2, 4, 5, 10, 11, 23, 25]
i = 9
while True:
    s = 0
    for x in neighbours(i):
        if x < len(l): s += l[x]
    l.append(s)
    if s > data:
        print(s)
        break
    i += 1

print("--- %s seconds ---" % (time.time() - start_time))