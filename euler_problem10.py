#!/usr/bin/python
#Filename: euler_problem10.py
from math import sqrt


def isprime(n):
    if n % 2 == 0:
        if n == 2:
            return True
        return False

    for i in range(2,int(sqrt(n) +1)):
        if n % i == 0:
            return False
    return True

primes = [ ]

for n in range(2,2000000):
    if isprime(n) == True:
        primes.append(n)

s = sum(primes)
print(s)
        
    
