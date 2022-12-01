import time
start_time = time.time()
d = open("8.txt").readlines(); 
# Part 1
"""count = 0
for l in d:
    l = l.split(" | ")
    f = l[1].split()
    count += sum([1 for e in f if len(e) < 5 or len(e) == 7])
print(count)"""

# Part 2
#d = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
result = 0
for l in d:
    l = l.split(" | ")
    f = [e.split() for e in l]
    enc = f[0]
    mapping = {}
    one = [set(x) for x in enc if len(x) == 2][0]
    seven = [set(x) for x in enc if len(x) == 3][0]
    four = [set(x) for x in enc if len(x) == 4][0]
    eight = [set(x) for x in enc if len(x) == 7][0]
    mapping["a"] = list(seven.difference(one))[0]
    mapping["b"] = four.difference(one)
    mapping["c"] = one
    mapping["d"] = four.difference(one)
    mapping["e"] = eight.difference(seven.union(four))
    mapping["f"] = one
    mapping["g"] = eight.difference(seven.union(four))
    six_segs = [set(x) for x in enc if len(x) == 6]

    for s in six_segs:
        # 9
        if isinstance(mapping["e"], set) and s == eight.difference(set(list(mapping["e"])[0])):
            mapping["g"] = list(mapping["e"])[1]
            mapping["e"] = list(mapping["e"])[0]
        elif isinstance(mapping["e"], set) and s == eight.difference(set(list(mapping["e"])[1])):
            mapping["g"] = list(mapping["e"])[0]
            mapping["e"] = list(mapping["e"])[1]
        # 0
        elif isinstance(mapping["d"], set) and s == eight.difference(set(list(mapping["d"])[0])):
            mapping["b"] = list(mapping["d"])[1]
            mapping["d"] = list(mapping["d"])[0]
        elif isinstance(mapping["d"], set) and s == eight.difference(set(list(mapping["d"])[1])):
            mapping["b"] = list(mapping["d"])[0]
            mapping["d"] = list(mapping["d"])[1]
        # 6
        elif isinstance(mapping["c"], set) and s == eight.difference(set(list(mapping["c"])[0])):
            mapping["f"] = list(mapping["c"])[1]
            mapping["c"] = list(mapping["c"])[0]
        elif isinstance(mapping["c"], set) and s == eight.difference(set(list(mapping["c"])[1])):
            mapping["f"] = list(mapping["c"])[0]
            mapping["c"] = list(mapping["c"])[1]
        else:
            print("Error")
    
    inv_map = {v: k for k, v in mapping.items()}
    
    def decode(enc_set):
        dec = set([inv_map[i] for i in list(enc_set)])
        if dec == {"c", "f"}: return "1"
        elif dec == {"a", "c", "d", "e", "g"}: return "2"
        elif dec == {"a", "c", "d", "f", "g"}: return "3"
        elif dec == {"b", "c", "d", "f"}: return "4"
        elif dec == {"a", "b", "d", "f", "g"}: return "5"
        elif dec == {"a", "b", "d", "e", "f", "g"}: return "6"
        elif dec == {"a", "c", "f"}: return "7"
        elif dec == {"a", "b", "c", "d", "e", "f", "g"}: return "8"
        elif dec == {"a", "b", "c", "d", "f", "g"}: return "9"
        elif dec == {"a", "b", "c", "e", "f", "g"}: return "0"
        raise ValueError()
    
    digits = [decode(set(e)) for e in f[1]]
    result += int("".join(digits))
print(result)
print("--- %s seconds ---" % (time.time() - start_time))