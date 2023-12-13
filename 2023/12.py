import time
from functools import cache
start_time = time.time()

with open("12.txt", "r") as file:
    lines = [line.strip().split() for line in file.readlines()]
    data = [[a, tuple(int(x) for x in b.split(","))] for a,b in lines]

@cache
def possibilities(line: str, known: tuple[int]) -> int:
    # print(line, known)
    if line == "": return 1 if len(known) == 0 else 0 # alles passt, das ist eine Möglichkeit
    if len(known) == 0: return 0 if "#" in line else 1 # alle bekannten aufgebraucht, wenn nur noch ? dann valide
    if line[0] == ".": return possibilities(line[1:], known) # ignoriere "."
    num = 0
    if line[0] == "?":
        num += possibilities(line[1:], known) # tu so als ob "?" ein "." ist, also ignorieren

    if not any(c=="." for c in line[:known[0]]): # ersten n Charaktere sind nur "?" und "#"
        if len(line) == known[0]: # Wenn gleich lang, dann kann alles genommen werden
            num += possibilities(line[known[0]+1:], known[1:]) # line ist leer, aber bei known kann noch etwas übrig sein
        if len(line) > known[0] and line[known[0]] != "#": # wenn mehr von line übrig ist als gerade gefordert, muss danach ein "." oder "?" sein, "#" darf nicht blockiert sein
            num += possibilities(line[known[0]+1:], known[1:]) # einen mehr wegnehmen von line, weil danach muss eins platz sein
    
    return num

print(sum(possibilities(line, known) for line, known in data))
print(sum(possibilities("?".join([line]*5), known*5) for line, known in data))

print(f"--- {(time.time() - start_time)} seconds ---")