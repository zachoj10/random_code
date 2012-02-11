#!/usr/bin/python
#Filename: euler_problem16.py

#variables used(p, j, q, l, i, z, x)

p = [ ] 

q = str(2**1000)
l = len(q)
for i in range(0,int(l)):
    z = q[i]
    x = int(z)
    p.append(x)

print(p)
j = sum(p)
print(j)
    
