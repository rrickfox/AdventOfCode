import time
start_time = time.time()

with open("16.txt") as file:
	text = file.readline().strip()

inp = bin(int(text, 16))[2:].zfill(len(text)*4)
# print(inp)

def decode_bits(arr: str):
	# print(arr)
	v = int("".join(arr[:3]), 2)
	# print("version: " + str(v) + ", opcode: " + "".join(arr[3:6]))
	if "".join(arr[3:6]) == "100": #literal
		# print("literal: ", end='')
		ret = ""
		firstBit = 1
		offset = 0
		while firstBit != "0":
			firstBit = arr[6+offset:7+offset]
			ret += arr[7+offset:11+offset]
			offset += 5
		# print(str(int(ret, 2)) + ", len: " + str(6+offset))
		# print("returning: " + str((v, 6+offset)))
		return (v, 6+offset)
	else: #operator
		# print("operator: ", end='')
		if arr[6:7] == "0": #15 bit numbers
			l = int(arr[7:22], 2) #num of bits in body
			# print("15bit num, bits in body: " + str(l))
			offset = 0
			ret = 0
			while offset < l:
				t = decode_bits(arr[22+offset:22+l])
				ret += t[0]
				offset += t[1]
			# print("returning: " + str((v+ret, 22+offset)))
			return (v+ret, 22+offset)
		else: # 11 bits with first 11 bits as num of packets
			l = int(arr[7:18], 2) # num of sub-packets
			# print("11bit num, sub-packets: " + str(l))
			ret = 0
			offset = 0
			for _ in range(l):
				t = decode_bits(arr[18+offset:])
				ret += t[0]
				offset += t[1]
			# print("returning: " + str((v+ret, 18+offset)))
			return (v+ret, 18+offset)

print(decode_bits(inp)[0])

print("--- %s seconds ---" % (time.time() - start_time))