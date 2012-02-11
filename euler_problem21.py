#!/usr/bin/python
#Filename: euler_problem21.py

#variables used(n, s, p, i, x,)

numbs = { }
sums = { }


n = [ ]
s = 284

for p in xrange(1,10001):
    hello = [ ] 
    for i in xrange(2,p):
        if p % i == 0:
            hello.append(i)
    numbs[p] = hello
            
    #sums = sum(numbs[p])
    #print(sums)


##for i in numbs:
##    print i, numbs[i]

for i in numbs:
    sums[i] = sum(numbs[i])


##for i in sums:
##    print i,':', sums[i]

compare = [ ] 

for i in range(1,10001):
    for x in range(1,10001):
        if numbs[i] == sums[x] and numbs[x] == sums[i]:
            zoo = (numbs[i],numbs[x])
            compare.append(zoo)

print('compare equals', compare)
        
