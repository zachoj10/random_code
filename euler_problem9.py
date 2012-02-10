#!/usr/bin/python
#Filename: euler_problem9
from math import sqrt

cs = [ ] 
ass = [ ]
bs = [ ] 
for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if a+b+c == 1000:
                d = a**2+b**2
                if c == sqrt(d):
                    x = sqrt(d)
                    cs.append(x)
                    ass.append(a)
                    bs.append(b)
            

print(cs)
print(ass)
print(bs)
p = cs[0]*ass[0]*bs[0]
print(' The product of the pythagorean triplet equaling 1000 is,', p)


