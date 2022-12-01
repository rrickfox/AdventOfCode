# !!!!!!!!!!!!!!!!
# Does not work, goto both.py

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
# print(minXSteps)
maxXSteps = math.floor((math.sqrt(8*x1+1)-1)/2)
# print(maxXSteps)

numPossible = 0

for y in range(-200, 200):
	height = 0
	steps = 0
	if y >= 0:
		height = y*(y+1)//2
		steps += y + 1 # for 0
		minYSteps = math.ceil((math.sqrt(8*(-y0+height)+1)-1)/2)
		maxYSteps = math.floor((math.sqrt(8*(-y1+height)+1)-1)/2)
	else: 
		height = (-y)*((-y)+1)//2
		minYSteps = math.ceil((math.sqrt(8*(-y0+height)+1)-1)/2) + y -1
		maxYSteps = math.floor((math.sqrt(8*(-y1+height)+1)-1)/2) + y -1
	if minYSteps <= maxYSteps:
		if y >= 0:
			print(str(y) + " " + str(maxXSteps - minXSteps + 1))
			numPossible += maxXSteps - minXSteps + 1
		else:
			for steps in range(minYSteps, maxYSteps+1):
				for x in range(200):
					s = (x*(x+1)//2)-(max(x-steps, 0)*(max(x-steps, 0)+1)//2)
					if s >= x0 and s <= x1:
						print(str(y) + " " + str(x) + " (" + str(steps) + ") (" + str(s) + ")")
						numPossible += 1

print(numPossible)

print("--- %s seconds ---" % (time.time() - start_time))