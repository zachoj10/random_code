#!/usr/bin/python
#Filename: euler_problem21.py

#variables used(n, s, p, i, x,)

numbs = { }
##numbs represents all of the factors of a particular input
sums = { }
##sums represents the sum of all of the factors for a particular input



n = [ ]
s = 284

for p in range(1,10001):
    hello = [ ] 
    for i in range(1,p):
        if p % i == 0:
            hello.append(i)
    numbs[p] = hello
            
    #sums = sum(numbs[p])
    #print(sums)


##for i in numbs:
##    print(i, numbs[i])

for i in numbs:
    sums[i] = sum(numbs[i])


##for i in sums:
##    print(i,':', sums[i])

compare = [ ]
numbers = [ ] 

for z in range(1,10001):
    for x in range(1,10001):
        if z == sums[x]:
            if x == sums[z]:
                if x == z:
                    q = 0
                else:
                    zoo = (x,z)
                    paul = (x+z)
                    numbers.append(zoo)
                    compare.append(paul)

j = sum(compare)
b = j/2

print('the amicable pairs are', numbers)
print('the sum of the amicable pairs is', b)
