import time
start_time = time.time()
with open("8.txt") as file:
	lines = file.readlines()
	lines = [x.strip().split(" | ") for x in lines]

lines = [(line[0].split(" "), line[1].split(" ")) for line in lines]

# ExampleDigits = ["abcdeg", "ab", "acdfg", "abcdf", "abef", "bcdef", "bcdefg", "abd", "abcdefg", "abcdef"]
# => Get Digits for every line, save as segment to letter association

# first 1
# then 7 (one not in 1 is top)
# then 4
# then 0, uses only one of 4 - 1 (used one is top left, unused one is middle)
# then 6, uses only one of 1 (used one is bottom right, unused one is top right)
# then 9, last with 6 segments (6 - 9 is bottom left, other new is bottom)

# 7 segment:
#   0
# 1   2
#   3
# 4   5
#   6

# lookup for needed segments for each digit
sevenSegToDigit = ["012456", "25", "02346", "02356", "1235", "01356", "013456", "025", "0123456", "012356"]

sevenSegment = []

# calculate digits for every line using set operations
for line in lines:
	segments = [""] * 7
	one = set([x for x in line[0] if len(x) == 2][0])
	seven = set([x for x in line[0] if len(x) == 3][0])
	segments[0] = next(iter(seven - one))
	four = set([x for x in line[0] if len(x) == 4][0])
	zero = set([x for x in line[0] if len(x) == 6 and len(set(x) & (four - one)) == 1][0])
	segments[1] = next(iter(zero & (four - one)))
	segments[3] = next(iter((four - one) - (zero & (four - one))))
	six = set([x for x in line[0] if len(x) == 6 and len(set(x) & one) == 1][0])
	segments[5] = next(iter(six & one))
	segments[2] = next(iter(one - six))
	nine = set([x for x in line[0] if len(x) == 6 and set(x) != zero and set(x) != six][0])
	segments[4] = next(iter(six - nine))
	segments[6] = next(iter(nine - four - seven))
	sevenSegment.append(segments)

# look up every given pattern in conversion list
# generates a list like ExampleDigits
digits = [["".join(sorted([line[int(x)] for x in number])) for number in sevenSegToDigit] for line in sevenSegment]

# look up every given pattern in above, customized lookup
# convert list of digits to strings, join strings, convert to int
# print sum of all generated numbers
print(sum([int("".join([str(tup[1].index("".join(sorted(x)))) for x in tup[0][1]])) for tup in zip(lines, digits)]))
print("--- %s seconds ---" % (time.time() - start_time))