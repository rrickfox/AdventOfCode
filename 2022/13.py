import time, itertools, functools
start_time = time.time()

with open("13.txt", "r") as file:
    lines = file.read().split("\n\n")
    data = [(eval(line.split("\n")[0]), eval(line.split("\n")[1])) for line in lines]

def compare(pack1, pack2):
    if isinstance(pack1, int) and isinstance(pack2, int):
        return pack1 <= pack2, pack1 < pack2
    if isinstance(pack1, list) and isinstance(pack2, list):
        for p1, p2 in zip(pack1, pack2):
            t = compare(p1, p2)
            if not t[0] or t[1]:
                return t
        # no wrong or right value found, both were the same
        return len(pack1) <= len(pack2), len(pack1) < len(pack2)
    # one is int, other is list
    if isinstance(pack1, list) and isinstance(pack2, int):
        x = compare(pack1, [pack2])
        return x
    if isinstance(pack1, int) and isinstance(pack2, list):
        x = compare([pack1], pack2)
        return x
    print("====== unsupported type ======")

print(sum(i + 1 if compare(pack1, pack2)[0] else 0 for i, (pack1, pack2) in enumerate(data)))

all_packs = list(itertools.chain.from_iterable(data)) + [[[2]], [[6]]]
packs_sorted = sorted(all_packs, key = functools.cmp_to_key(lambda x, y: -1 if compare(x, y)[0] else 1))
index = 1
ret = 1
for pack in packs_sorted:
    if pack == [[2]] or pack == [[6]]:
        ret *= index
    index += 1

print(ret)


print("--- %s seconds ---" % (time.time() - start_time))