#!/usr/bin/python
#Filename: euler_problem20.py

from math import factorial

t = [ ] 

q = factorial(100)
s = str(q)
l = len(s)
for i in range(0,l):
    n = s[i]
    z = int(n)
    t.append(z)

v = sum(t)
print(v)
