#!/usr/bin/python
#Filename:euler_problem2

#f = second number
#j = first number

hello = [ ] 
evens = [ ]
#n = 1
f = 1
j = 0
z = 0

while True:
    #n += 1
    if f+j > 4000000:
        break
    else:
        z = f+j
        hello.append(z)
        j = f
        f = z
        
for i in hello:
    if i % 2 == 0:
        evens.append(i)

g = sum(evens)
print(g)
    
