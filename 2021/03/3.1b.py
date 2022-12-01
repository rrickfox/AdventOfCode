import os
import sys
a = [(1 if v >= 0 else 0) for v in [sum(x) for x in zip(*[[(int(i)-.5)*2 for i in line] for line in [list(line.strip()) for line in open(os.path.join(sys.path[0], "3.txt"), "r").readlines()]])]]
print(int("".join(str(v) for v in a), 2)*int("".join(str(1-v) for v in a), 2))