import time, re
import parse as p
start_time = time.time()

with open("04.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    # data = [len(set(l[0].split(" ")).intersection(set(l[1].split(" ")))) for line in lines if (l := re.sub("\s+", " ", line.split(": ")[1]).split(" | "))]
# print(sum([2**(p-1) for p in data if p > 0]))
# data = [len(set(l[0].split(" ")).intersection(set(l[1].split(" ")))) for line in open("04.txt", "r").readlines() if (l := re.sub("\s+", " ", line.strip().split(": ")[1]).split(" | "))]
data = [len(set(l[1].split()).intersection(set(l[2].split()))) for line in open("04.txt","r").readlines() if (l:=p.parse("Card {}: {} | {}\n", line))]
data = [sum(1 for x in l[1].split() if x in l[2].split()) for line in open("04.txt","r").readlines() if (l:=p.parse("Card {}: {} | {}\n", line))]
print(sum([2**(p-1) for p in data if p]))

num_cards = {}
res = 0
for i in range(len(data)):
    active = num_cards.get(i, 0) + 1
    res += active

    for p in range(data[i]):
        num_cards[i+p+1] = num_cards.get(i+p+1, 0) + active

print(res)

print(f"--- {(time.time() - start_time)} seconds ---")