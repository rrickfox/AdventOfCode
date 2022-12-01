import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

with open("9.txt") as file:
	lines = file.readlines()
	lines = [[int(x) for x in line.strip()] for line in lines]

data = np.array(lines)
z = np.array(lines)
# print(z)

basins = {}
changed = False

for indexY, line in enumerate(lines):
	for indexX, x in enumerate(line):
		minimum = True;
		if indexY > 0 and x > lines[indexY-1][indexX]:
			minimum = False
		if indexX > 0 and x > line[indexX-1]:
			minimum = False
		if indexX < len(line)-1 and x > line[indexX+1]:
			minimum = False
		if indexY < len(lines)-1 and x > lines[indexY+1][indexX]:
			minimum = False
		if minimum:
			changed = True
			basins[(indexX, indexY)] = set([(indexX, indexY)])

def update_basins():
	global changed
	changed = False
	for basin in basins:
		pointsToAdd = set()
		for point in basins[basin]:
			# find points around, that are higher and not 9
			if point[1] > 0 and (point[0], point[1]-1) not in basins[basin] and lines[point[1]-1][point[0]] > lines[point[1]][point[0]] and lines[point[1]-1][point[0]] != 9:
				changed = True
				pointsToAdd.add((point[0], point[1]-1))
			if point[0] < len(lines[0])-1 and (point[0]+1, point[1]) not in basins[basin] and lines[point[1]][point[0]+1] > lines[point[1]][point[0]] and lines[point[1]][point[0]+1] != 9:
				changed = True
				pointsToAdd.add((point[0]+1, point[1]))
			if point[1] < len(lines)-1 and (point[0], point[1]+1) not in basins[basin] and lines[point[1]+1][point[0]] > lines[point[1]][point[0]] and lines[point[1]+1][point[0]] != 9:
				changed = True
				pointsToAdd.add((point[0], point[1]+1))
			if point[0] > 0 and (point[0]-1, point[1]) not in basins[basin] and lines[point[1]][point[0]-1] > lines[point[1]][point[0]] and lines[point[1]][point[0]-1] != 9:
				changed = True
				pointsToAdd.add((point[0]-1, point[1]))
		basins[basin].update(pointsToAdd)

# show hight map in 2d
fig = plt.figure()
plt.title('Basins as 2d heat map')
z[:] = -1
for key in set().union(*basins.values()):
	z[key] = data[key]
z = np.ma.masked_equal(z, -1)

p = plt.imshow(z, animated=True)
plt.colorbar(p)

first = True
changed = True

def updatefig(*args):
	global z, first
	if first:
		first = False
		z[:] = -1
		for key in set().union(*basins.values()):
			z[key] = data[key]
		z = np.ma.masked_equal(z, -1)
		p.set_array(z)
	elif changed:
		update_basins()
		z[:] = -1
		for key in set().union(*basins.values()):
			z[key] = data[key]
		z = np.ma.masked_equal(z, -1)
		p.set_array(z)
	else:
		z[:] = -1
		for key in set().union(*[basins[x[1]] for x in sorted(list([(len(basins[basin]), basin) for basin in basins]), reverse=True)[:3]]):
			z[key] = data[key]
		z = np.ma.masked_equal(z, -1)
		p.set_array(z)
	return p,

ani = animation.FuncAnimation(fig, updatefig, interval=500, blit=True)

# FFwriter = animation.FFMpegWriter(fps=2, extra_args=['-vcodec', 'libx264'])
# ani.save('animation.mp4', writer = FFwriter)


f = r"c://Users/Richa/OneDrive/Desktop/animation.gif"
writergif = animation.PillowWriter(fps=2)
ani.save(f, writer=writergif)

plt.show()