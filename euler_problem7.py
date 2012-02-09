#!/usr/bin/python
#Filename: euler_problem7
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

count = 2
primes = 0
while True:
    if isprime(count) == True:
        primes += 1
    if primes == 10001:
        print('The 10001th prime is', count)
        break
    count += 1
