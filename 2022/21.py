import time
start_time = time.time()

with open("21.txt", "r") as file:
    lines = [line.strip().split(": ") for line in file.readlines()]

data = {}
for line in lines:
    if line[1].isdigit():
        data[line[0]] = int(line[1])
    else:
        data[line[0]] = line[1].split(" ")

def get(key):
    if isinstance(data[key], int):
        return data[key]
    else:
        t = data[key]
        if t[1] == "+":
            return get(t[0]) + get(t[2])
        elif t[1] == "-":
            return get(t[0]) - get(t[2])
        elif t[1] == "/":
            return get(t[0]) // get(t[2])
        elif t[1] == "*":
            return get(t[0]) * get(t[2])
    print(data[key])

def get2(key):
    if isinstance(data[key], int) or isinstance(data[key], str):
        return data[key]
    else:
        t = data[key]
        op = t[1]
        term1, term2 = get2(t[0]), get2(t[2])
        if isinstance(term1, int) and isinstance(term2, int):
            if op == "+":
                return term1 + term2
            elif op == "-":
                return term1 - term2
            elif op == "/":
                return term1 // term2
            elif op == "*":
                return term1 * term2
        elif isinstance(term1, str) or isinstance(term1, tuple) or isinstance(term2, str) or isinstance(term2, tuple):
            return (op, term1, term2)
        else:
            print(f"Idk: {(op, term1, term2)}")
            return None

def equalize(term1, term2):
    # print(f"got {term1} and {term2}")
    if isinstance(term2, str):
        return term1
    elif isinstance(term1, str):
        return term2
    else:
        if isinstance(term1, int):
            op, t1, t2 = term2
            if isinstance(t1, int): # term1 = t1 op x (x = t2)
                if op == "+":
                    return equalize(term1 - t1, t2)
                elif op == "-":
                    return equalize(t1 - term1, t2)
                elif op == "/":
                    return equalize(t1 // term1, t2)
                elif op == "*":
                    return equalize(term1 // t1, t2)
            elif isinstance(t2, int): # term1 = x op t2 (x = t1)
                if op == "+":
                    return equalize(term1 - t2, t1)
                elif op == "-":
                    return equalize(term1 + t2, t1)
                elif op == "/":
                    return equalize(term1 * t2, t1)
                elif op == "*":
                    return equalize(term1 // t2, t1)
            else:
                print(f"Idk: {(term1, term2)}")
        elif isinstance(term2, int):
            op, t1, t2 = term1
            if isinstance(t1, int): # term1 = t1 op x (x = t2)
                if op == "+":
                    return equalize(term2 - t1, t2)
                elif op == "-":
                    return equalize(t1 - term2, t2)
                elif op == "/":
                    return equalize(t1 // term2, t2)
                elif op == "*":
                    return equalize(term2 // t1, t2)
            elif isinstance(t2, int): # term1 = x op t2 (x = t1)
                if op == "+":
                    return equalize(term2 - t2, t1)
                elif op == "-":
                    return equalize(term2 + t2, t1)
                elif op == "/":
                    return equalize(term2 * t2, t1)
                elif op == "*":
                    return equalize(term2 // t2, t1)
            else:
                print(f"Idk: {(term1, term2)}")

print(get("root"))

data["root"][1] = "="
data["humn"] = "x"
ast = get2("root")
print(equalize(ast[1], ast[2]))

print("--- %s seconds ---" % (time.time() - start_time))