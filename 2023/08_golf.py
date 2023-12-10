from math import*;x='\n';a,b=open("08.txt").read().split(x*2);l=[1 if c=="R" else 0 for c in a.strip()];m={i[0:3]:(i[7:10],i[12:15]) for i in b.split(x)};s='A'*3;i=0
while s!='Z'*3:s=m[s][l[i%len(l)]];i+=1
print(i);s=[n for n in m if n[-1]=='A'];c=1
for n in s:
    i=0
    while n[-1]!='Z':n=m[n][l[i%len(l)]];i+=1
    c=lcm(c,i)
print(c)
