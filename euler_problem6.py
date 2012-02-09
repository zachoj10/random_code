#!/usr/bin/python
#Filename: euler_problem6

#Variables used(i, j, k, x, l, p)

k = [ ]

#Sum of the sqaures of all number from 1 to 100
for i in range(1,101):
    j = i**2
    k.append(j)
x = sum(k)
print(x)

#Square of the sums of all of the numbers from 1 to 100
l = range(1,101)

p = sum(l)

a = p**2
print(a)


z = a-x
print(z)
