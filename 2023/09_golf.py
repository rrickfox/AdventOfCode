def p(l):
	if l==[0]:return 0,0
	s,e=p([a-b for a,b in zip(l[1:],l[:-1])]);return l[0]-s,l[-1]+e
x=y=0
for l in [list(map(int,l.split())) for l in open("09.txt").read().split("\n")]:
	a,b=p(l);x+=b;y+=a
print(x,y)