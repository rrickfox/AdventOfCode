import time, math
start_time = time.time()

with open("17.txt") as file:
	text = file.readline().strip()
	(tx0, tx1), (ty0, ty1) = ((int(xy[xy.index("=")+1:xy.index("..")]), int(xy[xy.index("..")+2:])) for xy in text.split(", "))

x0 = min(tx0, tx1)
x1 = max(tx0, tx1)
y0 = max(ty0, ty1)
y1 = min(ty0, ty1)

print("First: " + str((-y1-1)*(-y1)//2))

# calculate minimum steps to reach left border (using triangular-root)
minXSteps = math.ceil((math.sqrt(8*x0+1)-1)/2)
# calculate maximum steps before reaching right border (using triangular-root)
maxXSteps = math.floor((math.sqrt(8*x1+1)-1)/2)

# calculate all possible positive y values
positive_y = {int((2*y/ySteps -ySteps+1)//2): ySteps for ySteps in range(1, math.floor((math.sqrt(8*(-y1-1)+1)-1)//2)+1) for y in range(-y0-1, -y1) if (2*y/ySteps -ySteps +1)//2 >= 0}

# calculate num of steps to reach given point b with start-point a
steps = lambda a, b: 1/2 * (math.sqrt(4*a**2 -4*a +8*b +1) -2*a +1)
# dictionary of starting y velocities and a list of possible numbers of steps
positive_y_steps = {y: list(range(math.ceil(steps(y+1, -y0))+(2*y+1), math.floor(steps(y+1, -y1))+(2*y+1)+1)) for y in positive_y}
negative_y_steps = {-y-1: list(range(math.ceil(steps(y+1, -y0)), math.floor(steps(y+1, -y1))+1)) for y in positive_y}

both = (positive_y_steps | negative_y_steps)

numPossible = 0

for y in both:
	n = []
	for a in both[y]:
		if y >= 0 and a > maxXSteps:
			n += list(range(minXSteps, min(a, maxXSteps+1)))
		else:
			n += [int((-(a**2) + a + 2*b)/(2*a)+a-1) for b in range(x0, x1+1) if ((-(a**2) + a + 2*b)/(2*a)).is_integer()]
	numPossible += len(set(n))

print("Second: " + str(numPossible))

print("--- %s seconds ---" % (time.time() - start_time))