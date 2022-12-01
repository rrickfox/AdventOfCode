import time
from itertools import product
start_time = time.time()

with open("21.txt") as file:
	lines = file.readlines()
	p0_pos = int(lines[0].strip()[-1])
	p1_pos = int(lines[1].strip()[-1])

def encode_universe(s0, s1, p0, p1):
	return (s0 << 13) | (s1 << 8) | (p0 << 4) | p1

def decode_universe(h):
	return (h >> 13) & 0b11111, (h >> 8) & 0b11111, (h >> 4) & 0b1111, h & 0b1111

def step():
	global universes, turn, won0, won1
	temp = {}
	for hashed in universes:
		s0, s1, p0, p1 = decode_universe(hashed)
		if turn:
			for die in product([1, 2, 3], repeat=3):
				p = (p0 + sum(die) - 1) % 10 + 1
				if s0+p < 21:
					h = encode_universe(s0+p, s1, p, p1)
					temp[h] = temp.get(h, 0) + universes[hashed]
				else:
					won0 += universes[hashed]
		else:
			for die in product([1, 2, 3], repeat=3):
				p = (p1 + sum(die) - 1) % 10 + 1
				if s1+p < 21:
					h = encode_universe(s0, s1+p, p0, p)
					temp[h] = temp.get(h, 0) + universes[hashed]
				else:
					won1 += universes[hashed]
	universes = temp

universes = {encode_universe(0, 0, p0_pos, p1_pos): 1}
turn = True
won0 = won1 = 0

while len(universes) > 0:
	print(len(universes))
	step()
	turn = not turn

print(max(won0, won1))

print("--- %s seconds ---" % (time.time() - start_time))