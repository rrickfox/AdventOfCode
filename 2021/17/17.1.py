# !!!!!!!!!
# inefficient, goto both.py

import time, math
start_time = time.time()

with open("17.txt") as file:
	text = file.readline().strip()
	(tx0, tx1), (ty0, ty1) = ((int(xy[xy.index("=")+1:xy.index("..")]), int(xy[xy.index("..")+2:])) for xy in text.split(", "))

x0 = min(tx0, tx1)
x1 = max(tx0, tx1)
y0 = max(ty0, ty1)
y1 = min(ty0, ty1)

minXSteps = math.ceil((math.sqrt(8*x0+1)-1)/2)
maxXSteps = math.floor((math.sqrt(8*x1+1)-1)/2)

maxHeight = 0
p = []

for y in range(150):
	# print("===")
	height = 0
	steps = 0
	if y >= 0:
		height = y*(y+1)//2
		steps += y + 1 # for 0
		# print(height)
	minYSteps = math.ceil((math.sqrt(8*(-y0+height)+1)-1)/2)
	maxYSteps = math.floor((math.sqrt(8*(-y1+height)+1)-1)/2)
	if minYSteps <= maxYSteps:
		# print("trajectory possible")
		p.append(y)
		maxHeight = height if height > maxHeight else maxHeight

print(p)

# (2x+n-1)*n // 2 -> von x aus n schritte (x inklusive)
# a = (2x+n-1)*n // 2
# 2a = (2x+n-1)*n
# 2a/n = (2x+n-1)
# 2a/n -n+1 = 2x
# (2a/n -n+1)/2 = x

upperTrigRoot = lambda y: math.ceil((math.sqrt(8*(-y0+(y*(y+1)//2))+1)-1)/2)
lowerTrigRoot = lambda y: math.floor((math.sqrt(8*(-y1+(y*(y+1)//2))+1)-1)/2)

possible = [y-1 for y in range(-y0, -y1+1) if 2*y+2 > minXSteps] \
 + [y for y in range(-y0-1) if upperTrigRoot(y) <= lowerTrigRoot(y)]

print(possible)

print(sorted(possible) == p)

print(maxHeight)

# all needed for 1
print((-y1-1)*(-y1)//2)

print("--- %s seconds ---" % (time.time() - start_time))